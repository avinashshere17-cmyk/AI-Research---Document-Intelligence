from src.llm import ask_llm


question = "What is the main purpose of this project?"

context = """
This project is an AI-based research assistant that reads
PDFs, research papers, reports, and notes. It uses ML,
LLMs, and RAG to find useful information and answer
questions from documents.
"""


answer = ask_llm(question, context)

print("\nQUESTION:")
print(question)

print("\nANSWER:")
print(answer)