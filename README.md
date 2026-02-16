# KimiAI-Pro 🤖

<p align="center">✨ The Ultimate AI-Powered Workspace for Professional Human-AI Collaboration 💫</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Built%20With-Streamlit-FF4B4B?style=for-the-badge)
![Groq API](https://img.shields.io/badge/Powered%20By-Groq-black?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</p>

KimiAI Pro 🤖 – The ultimate AI-powered workspace. Multi-project chats 📜, real-time AI responses 🤖, PDF/TXT summarization 📜, and cutting-edge model support. Secure 🔒, lightning-fast 🚀, and engineered 🛠️ for seamless, professional human-AI collaboration 🤝.

KimiAI Pro is a high-end, multi-project AI workspace engineered for structured productivity and seamless human-AI collaboration.

Built with Streamlit and powered by advanced AI models, KimiAI Pro transforms simple chat interactions into organized, persistent, and professional AI workflows.

It is not just a chatbot.  
It is a **structured AI Operating Environment**.

## 📌 Table of Contents

- [Why KimiAI Pro](#-why-kimiaipro)
- [Core Features](#-core-features)
- [Installation](#-installation)
- [Architecture Overview](#-architecture-overview)
- [Usage](#-usage)
- [Supported Models](#-supported-models-)
- [Roadmap](#-roadmap)
- [Credits](#-credits)

# 🎯 Why KimiAI Pro?

Unlike basic AI chat applications, KimiAI Pro delivers:

- **🗂 Project-Based Architecture** – Structured AI workflows
- **💬 Persistent Multi-Chat System** – Organized conversations per project
- **⚡ Real-Time AI Streaming** – Instant response rendering
- **📄 Document-Aware Conversations** – TXT & PDF summarization
- **🎨 Premium UI/UX** – Gradient branding, glow effects, theme switching
- **🔐 Secure Access Control** – Session-based authentication
- **📦 Export & Backup Tools** – TXT export + JSON workspace backup

# 🚀 Core Features

- **🔐 Secure Login System:** Session-managed authentication with protected access.

- **🗂 Multi-Project Workspace:** Create, switch, and manage multiple AI-driven projects.

- **🧠 Custom System Prompts:** Fine-tune AI behavior per project environment.

- **📄 File Upload & Summarization:** Upload TXT or PDF files for AI-powered document insights.

- **🤖 Advanced Model Selection:**
  Supports the following high-performance models:
    - `moonshotai/kimi-k2-instruct-0905`
    - `llama3-70b-8192`
    - `mixtral-8x7b-32768`

- **Real-Time AI 🤖 Streaming:** Chat responses stream live for a smooth conversational experience.

- **🌗 Light & Dark Theme:** Professional theming for enhanced usability.

- **📤 Chat Export & Backup:** Download conversations as TXT or save the full workspace state as JSON.

- **Elegant UI:** Gradient headers, glowing chat bubbles, and sleek design for professional aesthetics.

# 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/hemant467/KimiAI-Pro.git
cd KimiAI-Pro
```

2. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv venv
```
  - macOS / Linux
```bash
source venv/bin/activate  # Linux / macOS
```
  - Windows
```bash
venv\Scripts\activate     # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
  - Create a `.env` file and add your Groq API key:

```bash
GROQ-API-KEY=your_api_key_here
```

5. Run the Application:
```bash
streamlit run "Code 📟/Kimi_App.py"
```

# 🔒 Login Credentials

<img width="1365" height="767" alt="Result - 1" src="https://github.com/user-attachments/assets/bfea2091-e312-4981-a036-fdae83d19e97" />

For demo purposes:

  - Username: `HemantKimi`
  - Password: `Kimi@123`

⚠️ Replace with secure authentication for production environments.

# ⚙️ Architecture Overview

```pgsql
User Interface (Streamlit)
        ↓
Session State Management
        ↓
Project / Chat Controller
        ↓
Groq API (LLM Streaming)
        ↓
Real-Time Token Rendering
```

This modular structure allows:

- Persistent memory per chat

- Dynamic system prompts

- Expandable model integration

# ⚡ Usage

- Select or create a project in the sidebar.

<img width="1365" height="767" alt="Result - 4" src="https://github.com/user-attachments/assets/a99d350b-7b9b-4c54-bd3e-80badeb215e0" />

- Customize the system prompt if desired.

- Start a chat or create a new one.

<img width="1365" height="767" alt="Result - 5" src="https://github.com/user-attachments/assets/410c1e1d-d352-45d9-899d-da5cbc156aed" />

- Upload TXT/PDF files for AI summarization.

<img width="1365" height="767" alt="Result - 15" src="https://github.com/user-attachments/assets/ca9d9072-2221-44c6-ad98-9e12fc9d8cfc" />

<img width="1365" height="767" alt="Result - 16" src="https://github.com/user-attachments/assets/b223e5bb-397f-4a4e-aeb6-4535b16054a2" />

- Interact with the AI and receive real-time responses.

<img width="1365" height="767" alt="Result - 6" src="https://github.com/user-attachments/assets/3fa71769-8d65-4f33-91f2-b12472e370e5" />

<img width="1365" height="767" alt="Result - 7" src="https://github.com/user-attachments/assets/3bcbfad3-459c-44f7-b9ad-2831610b8bf9" />

- Export chats as TXT or save workspace as JSON.

<img width="1365" height="767" alt="Result - 20" src="https://github.com/user-attachments/assets/15a1a6d5-b69c-4b8f-8cff-27f0cbc6f528" />

# 🌐 Supported Models 🤖

| Model Name                         | Description                           |
| ---------------------------------- | ------------------------------------- |
| `moonshotai/kimi-k2-instruct-0905` | Custom instruction-following model    |
| `llama3-70b-8192`                  | Large-scale general-purpose AI        |
| `mixtral-8x7b-32768`               | High-context multi-turn conversations |

# 💡 Future Improvements ✨

- Implement secure, hashed login system.

- Add chunked document processing for large PDFs.

- Integrate database storage for scalable multi-user environments.

- Add avatars and enhanced UI/UX for professional dashboards.

# 💻 Tech Stack

| Layer        | Technology Used |
| ------------ | --------------- |
| Frontend     | Streamlit       |
| Backend      | Python          |
| AI Engine    | Groq API        |
| File Parsing | PyPDF2          |
| Env Config   | Python dotenv   |

# 📈 Roadmap

- 🔒 Hashed authentication system

- 🧩 Chunked PDF processing for large documents

- 🗄 Database-backed persistence layer

- 🌍 Multi-user SaaS deployment

- 📊 Usage analytics dashboard

# 💖 Credits

Designed & Developed by `💖 Hemant Katta 💝`

# 🧠 Final Thoughts 💡 

KimiAI Pro 🤖 is more than a chatbot —
it is a structured AI productivity system built with scalability and professional workflows in mind ✨.

<img src="https://readme-typing-svg.herokuapp.com/?lines=KimiAI+Pro+🤖;The+Ultimate+AI-Powered+Workspace;Designed+%26+Developed+by+💖+Hemant+Katta+💝&font=Fira%20Code&color=%23FFD700&center=true&width=700&height=120&size=24">

<p align="center"><a href="https://github.com/hemant467/KimiAI-Pro">💖 Hemant Katta 💝</a></p>
