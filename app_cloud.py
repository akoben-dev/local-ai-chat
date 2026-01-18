import streamlit as st

st.set_page_config(page_title="Local AI Chat", page_icon="💬")
st.title("Local AI Chat (Demo)")

st.markdown("""
This is a **demo UI** of your local AI chat app.

- The full version runs **locally** on your Mac with **qwen3:14b** and PDF RAG.
- This cloud demo shows the **chat interface** and a **simulated RAG mode**.
- For real AI + document answers, run the local version.
""")

# Sidebar: mode + fake upload status
with st.sidebar:
    st.markdown("### 🎛️ Mode")
    rag_mode = st.toggle("RAG Mode (simulate PDF RAG)", value=False)

    st.markdown("### 📚 Document Status")
    if rag_mode:
        st.success("Simulating: '200-page ebook loaded and indexed.'")
        st.caption("In the local app, this would come from your PDF + Chroma setup.")
    else:
        st.info("General chat mode (no docs).")

    st.markdown("---")
    st.markdown("### About this Demo")
    st.write("""
- **Frontend**: Streamlit chat UI
- **Backend (local real app)**: qwen3:14b via Ollama
- **Extras (local real app)**: PDF upload, embeddings, vector search

This cloud version **simulates** the behaviors without running a real model.
""")
    if st.button("Clear chat"):
        st.session_state.messages = []
        st.rerun()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Hi! I'm the demo version of your Local AI Chat.\n\n"
                "- Toggle **RAG Mode** in the sidebar to see simulated document retrieval.\n"
                "- Ask a question to see how the UI would behave."
            ),
        }
    ]

# Render chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Simple function to simulate RAG behavior
def simulate_rag_answer(user_input: str) -> str:
    fake_chunks = [
        "> Chunk 1 (p. 23): Discusses keto macros and protein targets.\n",
        "> Chunk 2 (p. 47): Covers remote work productivity tips.\n",
        "> Chunk 3 (p. 102): Talks about strength training split for 4–5 days/week.\n",
    ]
    retrieved = "\n".join(fake_chunks)

    answer = (
        "🔎 **Simulated RAG Retrieval**\n\n"
        "Retrieved the following 3 relevant chunks from your indexed document:\n\n"
        f"{retrieved}\n"
        "---\n"
        "🧠 **Simulated Answer**\n\n"
        f"You asked: `{user_input}`\n\n"
        "In the **local real app**, qwen3:14b would read these chunks and generate a precise answer.\n\n"
        "Here we're just demonstrating how the interface would look when using RAG."
    )
    return answer

# Simple function to simulate general chat behavior
def simulate_general_answer(user_input: str) -> str:
    answer = (
        "💬 **Simulated General Chat Response**\n\n"
        f"You said: `{user_input}`\n\n"
        "In the **local real app**, this reply would come from qwen3:14b running on your machine, "
        "optionally using your conversation history for context.\n\n"
        "This cloud demo only shows how the chat UI behaves."
    )
    return answer

# Chat input
if user_input := st.chat_input("Type a message..."):
    # Store user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Demo assistant response
    with st.chat_message("assistant"):
        with st.spinner("Simulating response..."):
            if rag_mode:
                demo_reply = simulate_rag_answer(user_input)
            else:
                demo_reply = simulate_general_answer(user_input)
            st.markdown(demo_reply)

    st.session_state.messages.append({"role": "assistant", "content": demo_reply})
