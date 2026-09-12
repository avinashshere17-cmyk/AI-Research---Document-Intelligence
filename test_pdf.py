from src.pdf_processor import extract_text_from_pdf
from src.text_cleaner import clean_text
from src.chunker import create_chunks
from src.embedder import create_embeddings
from src.vector_store import create_vector_store
from src.retriever import search_similar_chunks


pdf_path = "data/papers/research.pdf"

# 1. Extract PDF
pages = extract_text_from_pdf(pdf_path)

# 2. Clean text
for page in pages:
    page["text"] = clean_text(page["text"])

# 3. Create chunks
chunks = create_chunks(pages)

# 4. Create embeddings for chunks
texts = [chunk["text"] for chunk in chunks]
embeddings = create_embeddings(texts)

# 5. Create FAISS database
index = create_vector_store(embeddings)

# 6. User question
question = "What are the main objectives of this project?"

# 7. Create embedding for the question
question_embedding = create_embeddings([question])

# 8. Search for relevant chunks
results = search_similar_chunks(
    index,
    question_embedding,
    chunks,
    top_k=3
)

# 9. Display results
print("\nQUESTION:")
print(question)

print("\nRELEVANT CHUNKS:")

for i, result in enumerate(results):

    print("\n------------------------")
    print("RESULT:", i + 1)
    print("PAGE:", result["page"])
    print("DISTANCE:", result["distance"])
    print("TEXT:")
    print(result["text"])