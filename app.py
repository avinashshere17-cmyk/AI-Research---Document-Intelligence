import streamlit as st
# Chat history
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []
from src.pdf_processor import extract_text_from_pdf
from src.text_cleaner import clean_text
from src.chunker import create_chunks
from src.embedder import create_embeddings
from src.vector_store import create_vector_store
from src.retriever import search_similar_chunks
from src.llm import ask_llm


# -------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------

st.set_page_config(
    page_title="AI Research & Document Intelligence",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)


# -------------------------------------------------
# CUSTOM CSS
# -------------------------------------------------

st.markdown("""
<style>

.main {
    padding-top: 2rem;
}

.title {
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 18px;
    color: #9ca3af;
    margin-bottom: 30px;
}

.card {
    padding: 25px;
    border-radius: 15px;
    border: 1px solid #333842;
    background-color: #17191f;
    margin-top: 20px;
}

.source-card {
    padding: 15px;
    border-radius: 10px;
    border: 1px solid #333842;
    background-color: #17191f;
    margin-bottom: 10px;
}
 
.small-text {
    color: #9ca3af;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)


# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

with st.sidebar:
    st.markdown("### 👨‍💻 Built by")
    st.markdown("**Avinash Shere**")
    st.markdown("✉️ [Mail](mailto:avinashshere07@gmail.com)")
    st.markdown("🔗 [LinkedIn](https://www.linkedin.com/in/avinash-patil-b72aa3366?utm_source=share_via&utm_content=profile&utm_medium=member_android)")
    st.markdown("💻 [GitHub](https://github.com/avinashshere17-cmyk)")
    st.title("📚 Research Assistant")
    st.markdown("---")

    if st.button("🗑️ Reset Documents", use_container_width=True):
        st.session_state.clear()
        st.rerun()
    st.markdown("---")

    st.subheader("📄 Document")

    st.success("Research paper loaded")

    st.write("**File:** research.pdf")

    st.markdown("---")

    st.subheader("🧠 Technology")

    st.write("• PDF Processing")
    st.write("• Text Chunking")
    st.write("• Sentence Transformers")
    st.write("• FAISS Vector Search")
    st.write("• Gemini LLM")
    st.write("• RAG")

    st.markdown("---")

    st.caption("AI Research & Document Intelligence")
    st.caption("Powered by AI + RAG")


# -------------------------------------------------
# MAIN HEADER
# -------------------------------------------------

st.markdown(
    '<div class="title">📚 AI Research & Document Intelligence</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Ask questions and get intelligent answers from your research documents.'
    '</div>',
    unsafe_allow_html=True
)


# -------------------------------------------------
# UPLOAD MULTIPLE PDF DOCUMENTS
# -------------------------------------------------

st.subheader("📄 Upload Research Papers")

uploaded_files = st.file_uploader(
    "Upload one or more PDF files",
    type=["pdf"],
    accept_multiple_files=True
)


if uploaded_files:

    st.success(f"✅ {len(uploaded_files)} PDF(s) selected")

    for file in uploaded_files:
        st.write(f"📄 {file.name}")

    if st.button("⚡ Process Documents", use_container_width=True):

        all_pages = []

        with st.spinner("📚 Processing your research papers..."):

            for file in uploaded_files:

                # Save uploaded PDF temporarily
                temp_path = f"data/papers/{file.name}"

                with open(temp_path, "wb") as f:
                    f.write(file.getbuffer())

                # Extract text
                pages = extract_text_from_pdf(temp_path)

                # Add document name to every page
                for page in pages:

                    all_pages.append({
                        "page": page["page"],
                        "text": clean_text(page["text"]),
                        "document": file.name
                    })


            # Create chunks
            chunks = create_chunks(all_pages)

            # Create embeddings
            texts = [chunk["text"] for chunk in chunks]

            embeddings = create_embeddings(texts)

            # Create FAISS index
            index = create_vector_store(embeddings)


        # Store in session
        st.session_state["chunks"] = chunks
        st.session_state["index"] = index
        st.session_state["documents_processed"] = True

        st.success("🎉 Documents processed successfully!")


# Check whether documents are processed
if "documents_processed" not in st.session_state:

    st.info("👆 Upload your research papers and click 'Process Documents'.")

    st.stop()


# Retrieve processed data
chunks = st.session_state["chunks"]
index = st.session_state["index"]

# -------------------------------------------------
# DOCUMENT INFORMATION
# -------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
   st.metric("📄 Documents", len(uploaded_files))
with col2:
    st.metric("🧩 Text Chunks", len(chunks))

with col3:
    st.metric("🔍 Retrieval", "FAISS")


st.markdown("")


# -------------------------------------------------
# QUESTION SECTION
# -------------------------------------------------

st.subheader("🔎 Ask Questions About Your Documents")


  

selected_question = st.session_state.get("selected_question", "")

question = st.text_input(
    "Enter your question",
    value=selected_question,
    placeholder="Example: What is the main objective of this research paper?",
    label_visibility="collapsed"
)
if st.button("🤖 Ask AI", type="primary", use_container_width=True):
    ask_ai_clicked = True
else:
    ask_ai_clicked = False

# -------------------------------------------------
# RECOMMENDED QUESTIONS
# -------------------------------------------------

st.subheader("💡 Recommended Questions")

recommended_questions = [
    "What is the main objective of this research?",
    "What problem does this research address?",
    "What methodology is used?",
    "What are the key findings?",
    "What are the expected outcomes?",
    "What dataset is used?",
    "What are the limitations of this research?",
    "What are the advantages of the proposed approach?",
    "What algorithms are used?",
    "What are the future research directions?",
    "What are the important results?",
    "What conclusions are presented?",
    "What technologies are used?",
    "What is the research gap?",
    "How does this approach improve existing methods?",
    "What are the main contributions?",
    "What challenges are discussed?",
    "What are the practical applications?",
    "How was the proposed system evaluated?",
    "Give me a short summary of this research."
]

for i, question in enumerate(recommended_questions):

    if st.button(question, key=f"recommended_{i}"):
        st.session_state["selected_question"] = question
# -------------------------------------------------
# CHAT HISTORY
# -------------------------------------------------

if st.session_state["chat_history"]:

    st.subheader("💬 Chat History")

    for chat in st.session_state["chat_history"]:
        st.markdown("**👤 You:**")
        st.write(chat["question"])

        st.markdown("**🤖 AI:**")
        st.write(chat["answer"])

        st.markdown("---")
# -------------------------------------------------
# ASK AI
# -------------------------------------------------

if ask_ai_clicked:

    if question:

        # Create question embedding
        with st.spinner("🔍 Searching your documents..."):

            question_embedding = create_embeddings([question])

            results = search_similar_chunks(
                index,
                question_embedding,
                chunks,
                top_k=5
            )


        # Create context for Gemini
        context = "\n\n".join(
            [
                f"Document: {result.get('document', 'Research Paper')}\n"
                f"Page: {result['page']}\n"
                f"{result['text']}"
                for result in results
            ]
        )


        # Generate answer
        with st.spinner("🤖 Generating answer..."):

            answer = ask_llm(question, context)

        st.session_state["chat_history"].append({
            "question": question,
            "answer": answer
        })


        # -------------------------------------------------
        # ANSWER
        # -------------------------------------------------

        st.markdown("---")

        st.subheader("🤖 Answer")

        st.write(answer)


            # -------------------------------------------------
        # EXPORT REPORT
        # -------------------------------------------------

        report = f"""
AI Research & Document Intelligence
===================================

Question:
{question}

Answer:
{answer}

Sources:
"""

        for i, result in enumerate(results, start=1):
            document_name = result.get("document", "Research Paper")
            page_number = result["page"]

            report += f"""
Source {i}
Document: {document_name}
Page: {page_number}

{result["text"]}

-----------------------------------
"""

        st.download_button(
            "📥 Download Research Report",
            report,
            file_name="research_report.txt",
            mime="text/plain",
            use_container_width=True
        )

        # -------------------------------------------------
        # SOURCES
        # -------------------------------------------------

        st.subheader("📖 Sources")

        for i, result in enumerate(results, start=1):

            document_name = result.get(
                "document",
                "Research Paper"
            )

            page_number = result["page"]

            with st.expander(
                f"📄 Source {i} — {document_name} — Page {page_number}"
            ):

                st.write(result["text"])


else:

    st.warning("⚠️ Please enter a question first.")