import streamlit as st
from pathlib import Path

from src.chatbot import ask_question
from src.pipeline import rebuild_vector_database

# ----------------------------------------
# Page Configuration
# ----------------------------------------

st.set_page_config(
    page_title="AI College Assistant",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------
# Load CSS
# ----------------------------------------

css_file = Path(__file__).parent.parent / "assets" / "style.css"

with open(css_file) as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# ----------------------------------------
# Session State
# ----------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# ========================================
# SIDEBAR
# ========================================

with st.sidebar:

    st.title("🎓 AI College Assistant")

    st.markdown("---")

    # ===============================
    # Statistics
    # ===============================

    st.subheader("📊 Statistics")

    user_count = sum(
        1
        for message in st.session_state.messages
        if message["role"] == "user"
    )

    assistant_count = sum(
        1
        for message in st.session_state.messages
        if message["role"] == "assistant"
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Questions", user_count)

    with col2:
        st.metric("Answers", assistant_count)

    st.markdown("---")

    # ===============================
    # Upload PDF
    # ===============================

    st.subheader("📂 Upload PDF")

    uploaded_file = st.file_uploader(
        "Choose a PDF",
        type=["pdf"]
    )

    if uploaded_file is not None:

        save_path = Path("data") / uploaded_file.name

        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success(f"✅ {uploaded_file.name} uploaded!")

        if st.button(
            "⚙️ Process Documents",
            use_container_width=True
        ):

            with st.spinner("Building Vector Database..."):

                docs, chunks = rebuild_vector_database()

            st.success(
                f"Processed {docs} PDFs ({chunks} chunks)"
            )

    st.markdown("---")

    # ===============================
    # Loaded Documents
    # ===============================

    st.subheader("📚 Loaded Documents")

    pdf_files = sorted(Path("data").glob("*.pdf"))

    with st.expander(
        f"View Documents ({len(pdf_files)})",
        expanded=False
    ):

        if pdf_files:

            for pdf in pdf_files:
                st.success(f"📄 {pdf.name}")

        else:

            st.warning("No PDFs found.")

    st.markdown("---")

    # ===============================
    # Clear Chat
    # ===============================

    if st.button(
        "🗑 Clear Chat",
        use_container_width=True
    ):

        st.session_state.messages = []

        st.rerun()

    st.markdown("---")

    st.caption("Version 2.2")

    st.caption("Powered by")

    st.write("🐍 Python")
    st.write("🦜 LangChain")
    st.write("🤗 Hugging Face")
    st.write("📦 ChromaDB")
    st.write("✨ Gemini")

    # ==========================================================
# MAIN PAGE
# ==========================================================

st.title("🎓 AI College Assistant")

st.caption("Ask questions from your college documents")

st.markdown("---")

# ==========================================================
# Welcome Card
# ==========================================================

if len(st.session_state.messages) == 0:

    st.info(
        """
### 👋 Welcome!

Ask questions from your uploaded college documents.

#### Examples

- 📅 When do semester exams begin?
- 📚 Explain the attendance regulations.
- 📝 What are the exam rules?
- 🎓 Explain the AI syllabus.

Upload additional PDFs from the sidebar anytime.
"""
    )

# ==========================================================
# Chat History
# ==========================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])
    # ==========================================================
# CHAT INPUT
# ==========================================================

question = st.chat_input(
    "Ask your question..."
)

if question:

    # --------------------------
    # Store User Message
    # --------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    # --------------------------
    # Get AI Response
    # --------------------------

    with st.spinner("🤖 Thinking..."):

        try:

            answer = ask_question(
                question,
                st.session_state.messages
            )

        except Exception as e:

            answer = f"❌ Error:\n\n{e}"

    # --------------------------
    # Store Assistant Message
    # --------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    # Refresh UI
    st.rerun()