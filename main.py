quiz = [
    {
        "question": "What is the capital of France?",
        "choices": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "What is 2 + 2?",
        "choices": ["A. 3", "B. 4", "C. 5", "D. 6"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "choices": ["A. Harper Lee", "B. Mark Twain", "C. Ernest Hemingway", "D. F. Scott Fitzgerald"],
        "answer": "A"
    }
]

def run_quiz(quiz):
    score = 0
    for q in quiz:
        print(q["question"])
        for choice in q["choices"]:
            print(choice)
        answer = input("Your answer: ").upper()
        if answer == q["answer"]:
            score += 1
            print("Correct!\n")
        else:
            print(f"Wrong! The correct answer is {q['answer']}\n")
    print(f"Your final score is {score} out of {len(quiz)}")

# Run the quiz
run_quiz(quiz)
