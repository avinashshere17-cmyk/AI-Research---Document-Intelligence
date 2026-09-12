from src.pdf_processor import extract_text_from_pdf
from src.text_cleaner import clean_text
from src.chunker import create_chunks
from src.embedder import create_embeddings
from src.vector_store import create_vector_store
from src.retriever import search_similar_chunks
from src.llm import ask_llm


# 1. Load PDF
pdf_path = "data/papers/research.pdf"

pages = extract_text_from_pdf(pdf_path)


# 2. Clean text
for page in pages:
    page["text"] = clean_text(page["text"])


# 3. Create chunks
chunks = create_chunks(pages)

print(f"\nCreated {len(chunks)} chunks.")


# 4. Create embeddings
texts = [chunk["text"] for chunk in chunks]

embeddings = create_embeddings(texts)

print("Embeddings created successfully.")


# 5. Create FAISS vector store
index = create_vector_store(embeddings)

print("FAISS index created successfully.")


# 6. Ask user a question
question = input("\nAsk a question about the research paper: ")


# 7. Create embedding for question
question_embedding = create_embeddings([question])


# 8. Search similar chunks
results = search_similar_chunks(
    index,
    question_embedding,
    chunks,
    top_k=3
)


# 9. Build context
context = "\n\n".join(
    [
        f"Page {result['page']}:\n{result['text']}"
        for result in results
    ]
)


# 10. Ask Gemini
answer = ask_llm(question, context)


# 11. Display answer
print("\n==============================")
print("ANSWER")
print("==============================")
print(answer)


# 12. Display sources
print("\n==============================")
print("SOURCES")
print("==============================")

for result in results:
    print(f"Page {result['page']}")