quiz = {
    "What is the capital of India?": ["a) Mumbai", "b) New Delhi", "c) Kolkata", "b"],
    "Who is the Chief Minister of Karnataka?": ["a) Basavaraj Bommai", "b) Siddaramaiah", "c) Yogi Adityanath", "b"]
}

score = 0

for question, options in quiz.items():
    print(question)
    for option in options[:-1]:
        print(option)
    answer = input("Your answer: ").lower()
    if answer == options[-1]:
        print("Correct!\n")
        score += 1
    else:
        print("Wrong!\n")

print(f"Your score: {score}/{len(quiz)}")