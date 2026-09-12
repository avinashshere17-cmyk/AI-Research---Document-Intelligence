def create_chunks(pages, chunk_size=1000, overlap=200):
    """
    Split page text into smaller overlapping chunks.

    Args:
        pages: List of page dictionaries.
        chunk_size: Maximum characters in each chunk.
        overlap: Characters shared between consecutive chunks.

    Returns:
        List of chunks containing text and page number.
    """

    chunks = []

    for page in pages:

        text = page["text"]
        page_number = page["page"]

        start = 0

        while start < len(text):

            end = start + chunk_size

            chunk_text = text[start:end]

            if chunk_text.strip():

                chunks.append({
                    "text": chunk_text,
                    "page": page_number
                })

            start += chunk_size - overlap

    return chunks