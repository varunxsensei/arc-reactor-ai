\documentclass[12pt]{article}
\usepackage{geometry}
\usepackage{xcolor}
\usepackage{hyperref}
\usepackage{amsmath}
\usepackage{listings}
\usepackage{graphicx}
\usepackage{parskip}
\geometry{margin=1in}

\hypersetup{
    colorlinks=true,
    linkcolor=cyan,
    filecolor=magenta,      
    urlcolor=cyan,
}

\title{\Huge \textbf{⚡ Arc Reactor AI}}
\author{}
\date{}

\begin{document}

\maketitle

\begin{center}
\Large A glowing, futuristic chat assistant powered by \textbf{GPT-4o + LangChain}, with domain-specific intelligence, persistent memory, and a beautiful \textbf{Streamlit UI}.
\end{center}

\vspace{1cm}

\section*{✨ Features}

\begin{itemize}
    \item 🧠 Chat with an AI expert in \textbf{any domain} you define (e.g., \texttt{Finance}, \texttt{Physics}, \texttt{Design}, etc.)
    \item 💬 Persistent \textbf{chat history} saved locally as \texttt{chat\_history.txt}
    \item 📐 Supports \LaTeX-style \textbf{math rendering} for technical responses
    \item ⚙️ Built using \textbf{LangChain} and \textbf{OpenAI GPT-4o}
    \item 🌌 Designed with a \textbf{neon-holographic Arc Reactor} theme via Streamlit CSS
    \item 🎯 Modular and easy to extend
\end{itemize}

\section*{🚀 Demo}

Coming soon: GIF or screenshot preview.

\section*{🛠️ Setup}

\subsection*{1. Clone the Repository}
\begin{lstlisting}[language=bash]
git clone https://github.com/yourusername/arc-reactor-ai.git
cd arc-reactor-ai
\end{lstlisting}

\subsection*{2. Install Dependencies}
\begin{lstlisting}[language=bash]
pip install -r requirements.txt
\end{lstlisting}

\subsection*{3. Configure API Key}
Create a \texttt{.env} file with your OpenAI API key:
\begin{lstlisting}
OPENAI_API_KEY=your_openai_key_here
\end{lstlisting}

\subsection*{4. Run the App}
\begin{lstlisting}[language=bash]
streamlit run app.py
\end{lstlisting}

\section*{📦 Folder Structure}
\begin{verbatim}
arc-reactor-ai/
├── app.py
├── chat_history.txt
├── .env
├── requirements.txt
└── README.md
\end{verbatim}

\section*{🧩 Tech Stack}
\begin{itemize}
    \item \href{https://streamlit.io/}{Streamlit} – for the web UI
    \item \href{https://www.langchain.com/}{LangChain} – for prompt templating and memory
    \item \href{https://platform.openai.com/docs}{OpenAI GPT-4o} – the LLM engine
\end{itemize}

\section*{💡 Use Cases}
\begin{itemize}
    \item Ask domain-specific questions (e.g., ``As a biology expert, explain CRISPR'')
    \item Explore ideas, troubleshoot code, or chat casually
    \item Learn math, physics, or ML with \LaTeX-rendered outputs
\end{itemize}

\section*{📜 License}
\textbf{MIT License} – open source and free to modify.

\section*{🧠 Future Ideas}
\begin{itemize}
    \item Add audio input/output
    \item Use local LLMs (Mistral, LLaMA via Ollama)
    \item Deploy online with GitHub Actions
    \item UI upgrade with animations and 3D background
\end{itemize}

\end{document}
