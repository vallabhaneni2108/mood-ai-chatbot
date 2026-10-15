
import streamlit as st
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

load_dotenv()

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Mood AI",
    page_icon="🎭",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ==================================================
# UI DESIGN
# ==================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

:root {
    --ink: #242139;
    --muted: #77758b;
    --purple: #7655df;
    --line: #e9e6f1;
    --surface: #ffffff;
}

.stApp {
    background: #f7f6fb !important;
    color: var(--ink) !important;
    font-family: 'DM Sans', sans-serif;
}

[data-testid="stHeader"] {
    background: transparent !important;
}

.block-container {
    max-width: 820px;
    padding-top: 1.8rem;
    padding-bottom: 3rem;
}

/* Header */

.topbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-bottom: 22px;
    border-bottom: 1px solid #e8e4f0;
    margin-bottom: 28px;
}

.brand {
    display: flex;
    align-items: center;
    gap: 11px;
}

.brand-icon {
    width: 43px;
    height: 43px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 14px;
    background: #7655df;
    color: white;
    font-size: 23px;
    box-shadow: 0 5px 15px #7655df25;
}

.brand-name {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 21px;
    font-weight: 800;
    letter-spacing: -0.8px;
    color: #28243f;
}

.brand-tagline {
    font-size: 11px;
    color: #858197;
    margin-top: 2px;
}

.header-pill {
    background: #eeebfa;
    border: 1px solid #e2dcf8;
    color: #6446c1;
    padding: 7px 11px;
    border-radius: 30px;
    font-size: 11px;
    font-weight: 600;
}

/* Welcome heading */

.eyebrow {
    color: #7655df;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 10px;
}

.hero-title {
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #25213c;
    font-size: clamp(28px, 5vw, 39px);
    line-height: 1.2;
    font-weight: 800;
    letter-spacing: -1.5px;
    margin-bottom: 11px;
}

.hero-description {
    color: #77758b;
    font-size: 14px;
    line-height: 1.8;
    margin-bottom: 27px;
}

/* Section labels */

.section-label {
    color: #38344e;
    font-size: 13px;
    font-weight: 700;
    margin-bottom: 10px;
}

/* Personality selector */

div[role="radiogroup"] {
    display: flex;
    gap: 10px;
    width: 100%;
}

div[role="radiogroup"] > label {
    flex: 1;
    min-width: 0;
    background: #ffffff !important;
    border: 1px solid #e6e2ef !important;
    border-radius: 15px !important;
    padding: 13px 9px !important;
    transition: all 0.2s ease;
}

div[role="radiogroup"] > label:hover {
    border-color: #a697e9 !important;
    background: #faf9ff !important;
}

div[role="radiogroup"] > label:has(input:checked) {
    background: #f0ecff !important;
    border: 1px solid #8a70e5 !important;
    box-shadow: 0 0 0 2px #7655df12;
}

div[role="radiogroup"] label p {
    color: #38334e !important;
    font-size: 12px !important;
    font-weight: 700 !important;
}

div[role="radiogroup"] input {
    accent-color: #7655df !important;
}

/* Selected personality information */

.selected-mode {
    display: flex;
    align-items: center;
    gap: 12px;
    background: #ffffff;
    border: 1px solid #e9e5f2;
    border-radius: 13px;
    padding: 12px 15px;
    margin-top: 12px;
    margin-bottom: 25px;
}

.selected-emoji {
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #f1edff;
    border-radius: 12px;
    font-size: 22px;
}

.selected-name {
    color: #302b46;
    font-size: 13px;
    font-weight: 700;
}

.selected-desc {
    color: #88849b;
    font-size: 12px;
    margin-top: 3px;
}

/* Conversation heading */

.conversation-header {
    display: flex;
    align-items: center;
    gap: 11px;
    margin-bottom: 14px;
}

.conversation-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 38px;
    height: 38px;
    background: #ebe6ff;
    border-radius: 12px;
    font-size: 19px;
}

.conversation-title {
    color: #302b46;
    font-size: 15px;
    font-weight: 700;
}

.conversation-caption {
    color: #89859b;
    font-size: 11px;
    margin-top: 3px;
}

/* Messages */

[data-testid="stChatMessage"] {
    background: #ffffff !important;
    border: 1px solid #eae6f1 !important;
    border-radius: 16px !important;
    padding: 14px 16px !important;
    margin-bottom: 11px !important;
    box-shadow: 0 3px 12px #29204405;
}

[data-testid="stChatMessage"]:has(
    [data-testid="chatAvatarIcon-user"]
) {
    background: #f0edff !important;
    border-color: #e1dafb !important;
}

[data-testid="stChatMessageContent"],
[data-testid="stChatMessageContent"] p {
    color: #302d42 !important;
    font-size: 14px !important;
    line-height: 1.8 !important;
}

/* Composer container */

.composer-label {
    font-size: 12px;
    font-weight: 700;
    color: #49435f;
    margin: 20px 0 8px;
}

/* Make the actual input clearly readable */

div[data-testid="stTextInput"] > div {
    background: #ffffff !important;
    border: 1px solid #dcd6eb !important;
    border-radius: 13px !important;
    box-shadow: 0 3px 12px #29204408 !important;
}

div[data-testid="stTextInput"] > div:focus-within {
    border-color: #8b70e8 !important;
    box-shadow: 0 0 0 3px #7655df15 !important;
}

div[data-testid="stTextInput"] input,
div[data-testid="stTextInput"] input:focus {
    background: #ffffff !important;
    color: #25213c !important;
    -webkit-text-fill-color: #25213c !important;
    caret-color: #7655df !important;
    opacity: 1 !important;
    font-size: 14px !important;
}

div[data-testid="stTextInput"] input::placeholder {
    color: #89849c !important;
    -webkit-text-fill-color: #89849c !important;
    opacity: 1 !important;
}

/* Send button */

div[data-testid="stFormSubmitButton"] button {
    min-height: 43px;
    background: #7655df !important;
    border: 1px solid #7655df !important;
    border-radius: 12px !important;
    color: #ffffff !important;
    font-size: 13px !important;
    font-weight: 700 !important;
    transition: background 0.2s ease;
}

div[data-testid="stFormSubmitButton"] button:hover {
    background: #6442cb !important;
    border-color: #6442cb !important;
}

div[data-testid="stFormSubmitButton"] button p {
    color: #ffffff !important;
}

/* Empty conversation */

.empty-state {
    text-align: center;
    background: #ffffff;
    border: 1px solid #e9e5f2;
    border-radius: 17px;
    padding: 30px 18px;
    margin-bottom: 12px;
}

.empty-emoji {
    font-size: 31px;
    margin-bottom: 10px;
}

.empty-title {
    color: #302b46;
    font-size: 16px;
    font-weight: 700;
}

.empty-copy {
    color: #858197;
    font-size: 12px;
    line-height: 1.8;
    margin-top: 7px;
}

/* Footer */

.footer {
    text-align: center;
    color: #9a96a9;
    font-size: 11px;
    margin-top: 26px;
}

div[data-testid="stAlert"] {
    border-radius: 13px;
}

/* Mobile */

@media (max-width: 600px) {
    .block-container {
        padding: 1rem 0.8rem 2rem;
    }

    .hero-title {
        letter-spacing: -0.8px;
    }

    div[role="radiogroup"] {
        gap: 5px;
    }

    div[role="radiogroup"] > label {
        padding: 11px 3px !important;
    }

    div[role="radiogroup"] label p {
        font-size: 10px !important;
    }

    .header-pill {
        font-size: 10px;
        padding: 6px 8px;
    }
}
</style>
""", unsafe_allow_html=True)

# ==================================================
# HEADER
# ==================================================

st.markdown("""
<div class="topbar">
    <div class="brand">
        <div class="brand-icon">🎭</div>
        <div>
            <div class="brand-name">Mood AI</div>
            <div class="brand-tagline">A little personality goes a long way.</div>
        </div>
    </div>
    <div class="header-pill">✦ AI CHAT</div>
</div>

<div class="eyebrow">YOUR CONVERSATION, YOUR RULES</div>
<div class="hero-title">Who are you in the mood<br>to talk to?</div>
<div class="hero-description">
    Pick a personality. Send a message. See what happens.
</div>
""", unsafe_allow_html=True)

# ==================================================
# MODEL
# ==================================================

@st.cache_resource
def load_model():
    return ChatGroq(
        model="openai/gpt-oss-120b",
        temperature=0.9,
    )

model = load_model()

# ==================================================
# PERSONALITIES
# ==================================================

modes = {
    "😡 Angry Mode": {
        "prompt": (
            "you are an Angry AI agent. "
            "you respond aggressively and impatiently."
        ),
        "description": "Aggressive and impatient",
        "emoji": "😡",
    },
    "😂 Funny Mode": {
        "prompt": (
            "you are a very Funny Agent. "
            "you respond with humour and jokes."
        ),
        "description": "Humorous and playful",
        "emoji": "😂",
    },
    "😢 Sad Mode": {
        "prompt": (
            "you are a very sad agent. "
            "you should respond with very sorrow."
        ),
        "description": "Sorrowful and melancholic",
        "emoji": "😢",
    },
}

# ==================================================
# SESSION STATE
# ==================================================

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

# ==================================================
# PERSONALITY SELECTOR
# ==================================================

st.markdown(
    '<div class="section-label">01 &nbsp; Choose your personality</div>',
    unsafe_allow_html=True,
)

mode_names = list(modes.keys())

selected_mode = st.radio(
    "Personality",
    options=mode_names,
    index=mode_names.index(st.session_state.selected_mode),
    horizontal=True,
    label_visibility="collapsed",
    disabled=st.session_state.chat_ended,
    key="mode_selector",
)

if selected_mode != st.session_state.selected_mode:
    st.session_state.selected_mode = selected_mode

    # Keep existing conversation; update personality only.
    st.session_state.messages[0] = SystemMessage(
        content=modes[selected_mode]["prompt"]
    )

    st.rerun()

current_mode = modes[st.session_state.selected_mode]

st.markdown(
    f"""
    <div class="selected-mode">
        <div class="selected-emoji">{current_mode["emoji"]}</div>
        <div>
            <div class="selected-name">{st.session_state.selected_mode}</div>
            <div class="selected-desc">{current_mode["description"]}</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ==================================================
# CONVERSATION
# ==================================================

st.markdown("""
<div class="conversation-header">
    <div class="conversation-icon">💬</div>
    <div>
        <div class="conversation-title">02 &nbsp; Conversation</div>
        <div class="conversation-caption">Your chat appears below.</div>
    </div>
</div>
""", unsafe_allow_html=True)

chat_messages = [
    message
    for message in st.session_state.messages
    if isinstance(message, (HumanMessage, AIMessage))
]

if not chat_messages and not st.session_state.chat_ended:
    st.markdown(
        f"""
        <div class="empty-state">
            <div class="empty-emoji">{current_mode["emoji"]}</div>
            <div class="empty-title">Your chat starts here</div>
            <div class="empty-copy">
                Say hello, ask something, or start a random conversation.<br>
                Your selected AI personality is ready.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

for message in chat_messages:
    if isinstance(message, HumanMessage):
        with st.chat_message("user", avatar="🧑"):
            st.markdown(message.content)

    elif isinstance(message, AIMessage):
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(message.content)

# ==================================================
# MESSAGE COMPOSER
# ==================================================

if st.session_state.chat_ended:
    st.info("Conversation ended. Thanks for chatting! 👋")

else:
    st.markdown(
        '<div class="composer-label">03 &nbsp; Your message</div>',
        unsafe_allow_html=True,
    )

    with st.form("message_form", clear_on_submit=True):
        input_col, send_col = st.columns([5, 1])

        with input_col:
            prompt = st.text_input(
                "Message",
                placeholder="Type here... your AI is listening",
                label_visibility="collapsed",
                key="message_input",
            )

        with send_col:
            submitted = st.form_submit_button(
                "Send  ➤",
                use_container_width=True,
            )

    if submitted and prompt.strip():
        prompt = prompt.strip()

        if prompt == "0":
            st.session_state.chat_ended = True
            st.rerun()

        st.session_state.messages.append(
            HumanMessage(content=prompt)
        )

        with st.chat_message("user", avatar="🧑"):
            st.markdown(prompt)

        with st.chat_message("assistant", avatar="🤖"):
            with st.spinner("Thinking..."):
                response = model.invoke(st.session_state.messages)
                st.markdown(response.content)

        st.session_state.messages.append(
            AIMessage(content=response.content)
        )

        st.rerun()

# ==================================================
# FOOTER
# ==================================================

st.markdown("""
<div class="footer">
    MOOD AI &nbsp; · &nbsp; Powered by Groq, LangChain & Streamlit
</div>
""", unsafe_allow_html=True)
