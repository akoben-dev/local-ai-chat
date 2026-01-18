import streamlit as st

st.title("Local AI Chat")
st.markdown("### Production RAG App - **qwen3:14b Local Demo**")

st.info("""
**This cloud demo shows the UI.** 
Full local version runs **qwen3:14b** (14GB RAM) with:
- PDF RAG (200+ pages)
- Chroma vector database
- Hybrid general/RAG modes
""")

with st.sidebar:
    st.markdown("### 🎛️ Mode")
    st.toggle("RAG Mode (PDF only)", value=False, disabled=True)
    st.markdown("### 📚 PDF Upload")
    st.file_uploader("Upload PDF", type="pdf", disabled=True)
    st.button("Process PDF", disabled=True)

st.markdown("""
## 💼 Portfolio Project
**Built by Charleston, SC Software Engineer**

✅ **Modern Python/Streamlit**  
✅ **RAG pipeline** (PyPDF → Chroma → qwen3:14b)  
✅ **Vector embeddings** (sentence-transformers)  
✅ **Production UX** (session state, caching)

**Interview talking points:**
> "Built production RAG app handling 200+ page PDFs 
> using local 14B model. Deployed hybrid cloud/local versions."
""")