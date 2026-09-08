import ollama

from rag import search_documents
from memory import add_memory, get_memory
from tool import available_tools
from config import OLLAMA_MODEL, TOP_K


def get_answer(question):

    documents = search_documents(
        question,
        k=TOP_K
    )

    context = "\n\n".join(
        doc.page_content
        for doc in documents
    )

    memory = get_memory()

    previous_context = ""

    if memory:
        previous_context = "\nPrevious conversation:\n"

        for item in memory[-3:]:
            previous_context += (
                f"Student: {item['question']}\n"
                f"Assistant: {item['answer']}\n"
            )

    tools = available_tools()
    current_date = tools["current_date"]

    prompt = f"""
You are an AI Student Support Assistant for a college.

Answer the student's question using the provided
college document context.

Do not invent information.

If the answer is not available in the provided
college documents, say:

"Sorry, this information is not available
in the provided college documents."

Current date:
{current_date}

College document context:
{context}

{previous_context}

Student question:
{question}

Give a clear and student-friendly answer.
"""

    response = ollama.chat(
        model=OLLAMA_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    answer = response["message"]["content"]

    add_memory(question, answer)

    return answer