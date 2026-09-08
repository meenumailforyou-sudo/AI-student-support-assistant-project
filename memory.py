conversation_history = []


def add_memory(question, answer):
    conversation_history.append({
        "question": question,
        "answer": answer
    })


def get_memory():
    return conversation_history


def clear_memory():
    conversation_history.clear()