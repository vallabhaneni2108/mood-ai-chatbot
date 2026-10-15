
import streamlit as st
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.messages import (
    AIMessage,
    SystemMessage,
    HumanMessage
)

load_dotenv()

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Mood AI | Chat",
    page_icon="🎭",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0b1020, #15152b, #101827);
    color: #f8fafc;
}

.block-container {
    max-width: 850px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.hero {
    text-align: center;
    padding: 20px 10px 25px;
}

.hero-icon {
    font-size: 48px;
    margin-bottom: 8px;
}

.hero h1 {
    font-size: 38px;
    font-weight: 800;
    letter-spacing: -1px;
    margin-bottom: 8px;
    color: #ffffff;
}

.hero p {
    color: #a5b4c8;
    font-size: 15px;
}

.section-label {
    color: #a5b4c8;
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 1px;
    margin: 10px 0;
    text-transform: uppercase;
}

div[role="radiogroup"] {
    gap: 12px;
}

div[role="radiogroup"] label {
    background: #171f32;
    border: 1px solid #303b52;
    border-radius: 16px;
    padding: 14px 18px;
}

div[role="radiogroup"] label:hover {
    border-color: #8b5cf6;
}

[data-testid="stChatMessage"] {
    background: #171f30;
    border: 1px solid #2c3850;
    border-radius: 18px;
    padding: 15px;
    margin-bottom: 14px;
}

[data-testid="stChatInput"] {
    border-radius: 18px;
    border: 1px solid #39465e;
    background: #171f30;
}

[data-testid="stChatInput"]:focus-within {
    border-color: #8b5cf6;
    box-shadow: 0 0 0 1px #8b5cf6;
}

[data-testid="stChatInput"] textarea {
    color: #ffffff;
}

[data-testid="stChatMessageContent"] {
    color: #e5e7eb;
    line-height: 1.7;
    font-size: 15px;
}

div[data-testid="stAlert"] {
    border-radius: 14px;
}

.footer {
    text-align: center;
    color: #77849b;
    font-size: 12px;
    margin-top: 24px;
}

div[data-testid="stCaptionContainer"] {
    color: #a5b4c8;
}

</style>

<div class="hero">
    <div class="hero-icon">🎭</div>
    <h1>Mood AI</h1>
    <p>Three personalities. One AI. Choose your vibe.</p>
</div>
""", unsafe_allow_html=True)

# ---------------- MODEL ----------------

@st.cache_resource
def load_model():
    return ChatGroq(
        model="openai/gpt-oss-120b",
        temperature=0.9
    )

model = load_model()

# ---------------- AI MODES ----------------

modes = {
    "😡 Angry Mode": {
        "prompt": (
            "you are an Angry AI agent. "
            "you respond aggressively and impatiently."
        ),
        "description": "Aggressive, impatient responses",
    },
    "😂 Funny Mode": {
        "prompt": (
            "you are a very Funny Agent. "
            "you respond with humour and jokes."
        ),
        "description": "Humor, jokes and playful replies",
    },
    "😢 Sad Mode": {
        "prompt": (
            "you are a very sad agent. "
            "you should respond with very sorrow."
        ),
        "description": "Sorrowful, melancholic responses",
    },
}

# ---------------- SESSION STATE ----------------

if "selected_mode" not in st.session_state:
    st.session_state.selected_mode = "😂 Funny Mode"

if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(
            content=modes[st.session_state.selected_mode]["prompt"]
        )
    ]

if "chat_ended" not in st.session_state:
    st.session_state.chat_ended = False

# ---------------- MODE SELECTOR ----------------

st.markdown(
    '<div class="section-label">Choose your AI personality</div>',
    unsafe_allow_html=True
)

selected_mode = st.radio(
    "AI personality",
    options=list(modes.keys()),
    index=list(modes.keys()).index(
        st.session_state.selected_mode
    ),
    horizontal=True,
    label_visibility="collapsed",
    disabled=st.session_state.chat_ended
)

st.caption(modes[selected_mode]["description"])

# Update personality without deleting chat history
if selected_mode != st.session_state.selected_mode:
    st.session_state.selected_mode = selected_mode

    # Update only the system message
    st.session_state.messages[0] = SystemMessage(
        content=modes[selected_mode]["prompt"]
    )

    st.rerun()

st.markdown("---")

# ---------------- CHAT HEADER ----------------

st.markdown(
    f"### {selected_mode}",
)

st.caption("Your conversation")

# ---------------- DISPLAY CHAT HISTORY ----------------

for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        with st.chat_message("user", avatar="🧑"):
            st.markdown(message.content)

    elif isinstance(message, AIMessage):
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(message.content)

# ---------------- CHAT INPUT ----------------

if st.session_state.chat_ended:
    st.info("Conversation ended. Thanks for chatting! 👋")

else:
    prompt = st.chat_input(
        "Write your message...",
        key="chat_input"
    )

    if prompt:
        # Original exit command
        if prompt == "0":
            st.session_state.chat_ended = True
            st.rerun()

        # Store user message
        st.session_state.messages.append(
            HumanMessage(content=prompt)
        )

        with st.chat_message("user", avatar="🧑"):
            st.markdown(prompt)

        # Generate response
        with st.chat_message("assistant", avatar="🤖"):
            with st.spinner(
                f"{selected_mode.split(' ', 1)[1]} is responding..."
            ):
                response = model.invoke(
                    st.session_state.messages
                )
                st.markdown(response.content)

        # Store AI response
        st.session_state.messages.append(
            AIMessage(content=response.content)
        )

# ---------------- FOOTER ----------------

st.markdown("""
<div class="footer">
    Powered by Groq · LangChain · Streamlit
</div>
""", unsafe_allow_html=True)
