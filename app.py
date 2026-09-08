from receiver import get_answer


def main():
    print("=" * 55)
    print("        AI STUDENT SUPPORT SYSTEM")
    print("=" * 55)

    print("Ask questions about your college syllabus.")
    print("Type 'exit' to close.\n")

    while True:
        question = input("Student: ").strip()

        if question.lower() == "exit":
            print("\nThank you!")
            break

        if not question:
            continue

        try:
            answer = get_answer(question)
            print("\nAI:", answer)
            print()

        except Exception as e:
            print("\nError:", e)
            print()


if __name__ == "__main__":
    main()