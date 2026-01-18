import streamlit as st

st.set_page_config(page_title="Local AI Chat", page_icon="💬")
st.title("Local AI Chat (Demo)")

st.markdown("""
This is a **demo UI** of your local AI chat app.

- The full version runs **locally** on your Mac with **qwen3:14b** and PDF RAG.
- This cloud demo shows the **chat interface** and how users would interact with it.
- For real AI answers, run the local app on your machine.
""")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I'm the demo version of your Local AI Chat. Ask me something and I'll show how the UI behaves."}
    ]

# Render chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if user_input := st.chat_input("Type a message (demo only, no real AI here)..."):
    # Store user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Demo assistant response (no LLM, just a placeholder)
    demo_reply = (
        "This is the **cloud demo** responding.\n\n"
        "- On your local machine, this reply would come from **qwen3:14b**.\n"
        "- It would also use your **PDF RAG pipeline** when in RAG mode.\n\n"
        f"You said: '{user_input}'\n\n"
        "In the full local version, I'd answer this using the actual model."
    )
    st.session_state.messages.append({"role": "assistant", "content": demo_reply})
    with st.chat_message("assistant"):
        st.markdown(demo_reply)

# Sidebar info
with st.sidebar:
    st.markdown("### About this Demo")
    st.write("""
- **Frontend**: Streamlit chat UI
- **Backend (local version)**: qwen3:14b via Ollama
- **Extras (local)**: PDF upload, RAG, vector search

This cloud app is for **showing the interface** only.
Run the local version for real AI responses.
""")
    if st.button("Clear chat"):
        st.session_state.messages = []
        st.rerun()
