import streamlit as st
from groq import Groq
import os
import json
import time
from dotenv import load_dotenv
from PyPDF2 import PdfReader

load_dotenv()

# =============================
# ⚙️ PAGE CONFIG (top)
# =============================
st.set_page_config(page_title="KimiAI Pro 🤖", page_icon="🤖", layout="wide")

# =============================
# 🔐 LOGIN SYSTEM
# =============================
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

def login():
    # CSS to vertically center login form
    st.markdown(
        """
        <style>
        .login-container {
            display: flex;
            flex-direction: column;
            height: 5vh;
        }
        .login-title {
            font-size: 36px;
            font-weight: 700;
            margin-bottom: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    with st.container():
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        st.markdown('<div class="login-title">🔐 Login to ֎ KimiAI 🇦🇮</div>', unsafe_allow_html=True)
        username = st.text_input("Username 📜")
        password = st.text_input("Password 🔐", type="password")
        if st.button("Login ➡️"):
            if username == "HemantKimi" and password == "Kimi@123":
                st.session_state.authenticated = True
                st.session_state.user = username
                st.rerun()
            else:
                st.error("💀 Invalid credentials ☠️")
        st.markdown(
            "<p style='text-align:center; color:gray; font-size:14px; margin-top:20px;'>Designed & Developed by 💖 Hemant Katta 💝</p>",
            unsafe_allow_html=True
        )
        st.markdown('</div>', unsafe_allow_html=True)

if not st.session_state.authenticated:
    login()
    st.stop()

# =============================
# 🌌 APP HEADER (Gradient + Glow)
# =============================
st.markdown("""
<style>
.main-header {
    font-size: 48px;
    font-weight: 700;
    background: linear-gradient(90deg, #00F5A0, #7F00FF);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0px 0px 15px rgba(0, 255, 200, 0.4);
    margin-bottom: 5px;
}
.sub-header {
    font-size: 16px;
    color: rgba(180,180,180,0.8);
    margin-top: 0px;
    letter-spacing: 0.5px;
}
.chat-container {
    border-radius: 15px;
    padding: 10px;
}
.user-msg {
    background: rgba(255,255,255,0.1);
    padding: 10px;
    border-radius: 12px;
    color: #FFFFFF;
    margin: 5px 0;
}
.ai-msg {
    background: rgba(0,255,200,0.2);
    padding: 10px;
    border-radius: 12px;
    color: #00FFC8;
    margin: 5px 0;
    animation: typingEffect 0.1s linear;
}
@keyframes typingEffect {
    from {opacity:0;}
    to {opacity:1;}
}
</style>
<div style="padding-top:10px;">
    <div class="main-header">KimiAI 🤖 Bot</div>
    <div class="sub-header">Designed & Developed by 💖 Hemant Katta 💝</div>
</div>
""", unsafe_allow_html=True)

# =============================
# 🌙 THEME TOGGLE
# =============================
theme = st.sidebar.radio("Theme", ["Light", "Dark"])
if theme == "Dark":
    st.markdown("""
    <style>
        body { background-color:#0E1117; color:white; }
        .user-msg { background: rgba(255,255,255,0.1); color: #fff;}
        .ai-msg { background: rgba(0,255,200,0.2); color: #00FFC8;}
    </style>
    """, unsafe_allow_html=True)

# =============================
# 🧠 MODEL SELECTOR
# =============================
models = ["moonshotai/kimi-k2-instruct-0905","llama3-70b-8192","mixtral-8x7b-32768"]
selected_model = st.sidebar.selectbox("Select Model", models)

# =============================
# 🔒 LOGOUT BUTTON
# =============================
st.sidebar.markdown(
    f"<div style='margin-top:10px; margin-bottom:10px; font-size:14px; color:rgba(180,180,180,0.8);'>👤 Logged in as <b>{st.session_state.user}</b></div>",
    unsafe_allow_html=True
)
if st.sidebar.button("🔓 Logout"):
    st.session_state.authenticated = False
    st.session_state.user = None
    st.rerun()

# =============================
# 📁 PROJECT & CHAT STATE
# =============================
if "projects" not in st.session_state:
    st.session_state.projects = {"Default Project":{"system":"You are a helpful AI assistant.","Chat 1":[]}}
if "current_project" not in st.session_state:
    st.session_state.current_project = "Default Project"
if "current_chat" not in st.session_state:
    st.session_state.current_chat = "Chat 1"

# =============================
# 📁 PROJECT MANAGEMENT
# =============================
st.sidebar.title("Workspace")
new_project = st.sidebar.text_input("New Project Name")
if st.sidebar.button("➕ Create Project"):
    if new_project:
        st.session_state.projects[new_project] = {"system":"You are a helpful AI assistant.","Chat 1":[]}
        st.session_state.current_project = new_project
        st.session_state.current_chat = "Chat 1"
        st.rerun()

selected_project = st.sidebar.selectbox("Select Project", list(st.session_state.projects.keys()))
st.session_state.current_project = selected_project
project_data = st.session_state.projects[selected_project]

# =============================
# 🧩 SYSTEM PROMPT
# =============================
system_prompt = st.sidebar.text_area("System Prompt", value=project_data["system"])
project_data["system"] = system_prompt

# =============================
# 💬 CHAT MANAGEMENT
# =============================
chat_keys = [k for k in project_data.keys() if k!="system"]
if st.sidebar.button("📝 New Chat"):
    chat_name = f"Chat {len(chat_keys)+1}"
    project_data[chat_name] = []
    st.session_state.current_chat = chat_name
    st.rerun()

selected_chat = st.sidebar.selectbox("Select Chat", chat_keys)
st.session_state.current_chat = selected_chat
messages = project_data[selected_chat]

if st.sidebar.button("🗑️ Clear Chat"):
    project_data[selected_chat] = []
    st.rerun()

# =============================
# 📎 FILE UPLOAD
# =============================
uploaded_file = st.sidebar.file_uploader("Upload TXT/PDF", type=["txt","pdf"])
if uploaded_file:
    if uploaded_file.type=="text/plain":
        content = uploaded_file.read().decode("utf-8")
    else:
        reader = PdfReader(uploaded_file)
        content = ""
        for page in reader.pages:
            content += page.extract_text()
    messages.append({"role":"user","content":f"Summarize this document:\n\n{content[:4000]}"})

# =============================
# 💬 DISPLAY CHAT
# =============================
for msg in messages:
    cls = "user-msg" if msg["role"]=="user" else "ai-msg"
    st.markdown(f"<div class='{cls}'>{msg['content']}</div>", unsafe_allow_html=True)

prompt = st.chat_input("😇 Please enter 👨‍💻 your message 📜 here...")

# =============================
# 🤖 AI RESPONSE STREAM
# =============================
if prompt:
    messages.append({"role":"user","content":prompt})
    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_response = ""
        client = Groq(api_key=os.getenv("GROQ-API-KEY"))
        start_time = time.time()
        stream = client.chat.completions.create(
            model=selected_model,
            messages=[{"role":"system","content":system_prompt}] + messages,
            stream=True
        )
        for chunk in stream:
            if chunk.choices and chunk.choices[0].delta.content:
                token = chunk.choices[0].delta.content
                full_response += token
                placeholder.markdown(f"<div class='ai-msg'>{full_response}</div>", unsafe_allow_html=True)
        end_time = time.time()
        response_time = round(end_time-start_time,2)
        token_estimate = len(full_response.split())
        st.caption(f"⏱ {response_time}s | 📊 ~{token_estimate} tokens")
    messages.append({"role":"assistant","content":full_response})

# =============================
# 📥 EXPORT CHAT & SAVE JSON
# =============================
if st.sidebar.button("Export TXT"):
    chat_text = "\n\n".join([f"{m['role'].upper()}: {m['content']}" for m in messages])
    st.download_button("Download TXT", chat_text, file_name="chat.txt", mime="text/plain")

if st.sidebar.button("Save JSON"):
    with open("projects_backup.json","w") as f:
        json.dump(st.session_state.projects,f, indent=4)

# streamlit run Kimi_App.py