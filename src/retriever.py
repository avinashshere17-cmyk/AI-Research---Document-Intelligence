import numpy as np


def search_similar_chunks(index, query_embedding, chunks, top_k=3):
    """
    Find the most relevant chunks for a user question.
    """

    query_embedding = np.asarray(query_embedding).astype("float32")

    # FAISS expects a 2D array
    query_embedding = query_embedding.reshape(1, -1)

    # Search the vector database
    distances, indices = index.search(query_embedding, top_k)

    results = []

    for distance, index_number in zip(distances[0], indices[0]):

        if index_number == -1:
            continue

        results.append({
            "text": chunks[index_number]["text"],
            "page": chunks[index_number]["page"],
            "distance": float(distance)
        })

    return results