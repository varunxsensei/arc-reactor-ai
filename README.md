
# ⚡ Arc Reactor AI

A glowing, futuristic AI assistant built with **LangChain**, **GPT-4o**, and **Streamlit** — featuring domain-specific intelligence, chat memory, and math support inside a sci-fi holographic UI.

---

## ✨ Features

- 🧠 Chat with an AI expert in **any domain** (e.g., Physics, AI, Biology)
- 💬 Persistent **chat history** saved locally (`chat_history.txt`)
- 📐 Supports **LaTeX-style math rendering** (useful for equations)
- ⚙️ Built with **LangChain + OpenAI GPT-4o**
- 🌌 Designed with a **neon Arc Reactor-style UI** in Streamlit

---

## 🛠️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/arc-reactor-ai.git
cd arc-reactor-ai
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your OpenAI API key

Create a `.env` file in the project root:

```bash
OPENAI_API_KEY=your_openai_key_here
```

### 4. Run the app

```bash
streamlit run app.py
```

---

## 📂 Folder Structure

```
arc-reactor-ai/
├── app.py
├── chat_history.txt
├── .env
├── requirements.txt
└── README.md
```

---

## 🧩 Tech Stack

- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [OpenAI GPT-4o](https://platform.openai.com/docs)
- `.env` for secrets and `chat_history.txt` for state

---

## 📜 License

MIT — feel free to fork and enhance.

---

## 🧠 Future Ideas

- 🎙️ Voice input/output
- 🧠 Local LLM (Mistral, LLaMA via Ollama)
- 🔄 Full chat session save/load
- 🌐 Deployment to Hugging Face or Streamlit Cloud
