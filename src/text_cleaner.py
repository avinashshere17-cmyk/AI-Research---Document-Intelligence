import re


def clean_text(text):
    """
    Clean extracted PDF text.
    """

    # Replace multiple spaces and line breaks
    # with a single space
    text = re.sub(r"\s+", " ", text)

    # Remove spaces at the beginning and end
    text = text.strip()

    return text