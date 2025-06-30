import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Futuristic AI Chat", page_icon="🤖", layout="centered")

# OpenAI model
model = ChatOpenAI(model="gpt-4o")

# Template
template = ChatPromptTemplate.from_messages([
    ("system", "You are an AI expert in {domain}"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{query}")
])

# UI Layout

st.markdown("""
    <style>
    /* Full screen futuristic background (holographic/arc reactor style) */
    body, .stApp {
        background-image: radial-gradient(circle at center, #00f2ff 0%, #001f2f 80%);
        background-size: cover;
        background-attachment: fixed;
        color: #e0faff;
        font-family: 'Orbitron', sans-serif;
    }

    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');

    h1, h2, h3, .stMarkdown, .stText {
        color: #e0faff !important;
        text-shadow: 0 0 3px #00e6e6, 0 0 6px #00ffff;
    }

    .stTextInput, .stTextArea, .stButton button {
        background-color: rgba(0, 255, 255, 0.08) !important;
        color: #ffffff !important;
        border: 1px solid #00ffff !important;
        border-radius: 10px;
    }

    .stTextInput input, .stTextArea textarea {
        color: #ffffff !important;
        font-weight: 500;
    }

    .stButton button:hover {
        background-color: rgba(0, 255, 255, 0.2) !important;
        transition: 0.3s ease-in-out;
    }

    ::-webkit-scrollbar {
        width: 8px;
    }

    ::-webkit-scrollbar-thumb {
        background: #00ffff;
        border-radius: 4px;
    }

    .stChatMessage {
        background-color: rgba(0, 255, 255, 0.1);
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)



st.title("🤖 AI Expert Assistant")
st.markdown("Ask me anything in your chosen **domain of expertise**.")

# Domain selection
domain = st.text_input("Enter your domain", "Machine learning specialist")

# Load history
if "chat_history" not in st.session_state:
    chat_history = []
    try:
        with open("chat_history.txt", "r") as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if i % 2 == 0:
                    chat_history.append(HumanMessage(content=line.strip()))
                else:
                    chat_history.append(AIMessage(content=line.strip()))
    except FileNotFoundError:
        chat_history = []
    st.session_state.chat_history = chat_history

# User query
query = st.text_area("Your question", placeholder="Ask anything...")

if st.button("Send"):
    if query.strip():
        st.session_state.chat_history.append(HumanMessage(content=query))

        chain = template | model
        result = chain.invoke({
            "domain": domain,
            "chat_history": st.session_state.chat_history,
            "query": query
        })

        st.session_state.chat_history.append(AIMessage(content=result.content))

        # Save chat_history
        with open("chat_history.txt", "w") as f:
            for msg in st.session_state.chat_history:
                f.write(msg.content + "\n")

# current conversation
if len(st.session_state.chat_history) >= 2:
    st.subheader("💬 Chat")
    user_msg = st.session_state.chat_history[-2]
    ai_msg = st.session_state.chat_history[-1]

    if isinstance(user_msg, HumanMessage):
        st.markdown(f"🧑‍💻 **You**: {user_msg.content}")
    if isinstance(ai_msg, AIMessage):
        st.markdown(f"🤖 **AI**: {ai_msg.content}")
