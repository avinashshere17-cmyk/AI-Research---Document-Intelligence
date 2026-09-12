import os
from dotenv import load_dotenv
from google import genai


# Load variables from .env
load_dotenv()

# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Create Gemini client
client = genai.Client(api_key=api_key)


def ask_llm(question, context):
    """
    Send the user question and retrieved document context
    to Gemini and generate an answer.
    """

    prompt = f"""
You are an AI research assistant.

Answer the user's question using ONLY the information
provided in the research document context below.

If the answer is not present in the context, say:
"I could not find this information in the provided document."

Research Context:
{context}

User Question:
{question}

Give a clear and concise answer.
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text