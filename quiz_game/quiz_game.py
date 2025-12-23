# Quiz Game

quiz_data = [
    {
        "question": "Which planet is known as the 'Red Planet'?",
        "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "B",
        "answer_text": "Mars"
    },

    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
        "answer": "D",
        "answer_text": "Pacific Ocean"
    },

    {
        "question": "Who is credited with inventing the telephone?",
        "options": ["A) Thomas Edison", "B) Nikola Tesla", "C) Alexander Graham Bell", "D) Benjamin Franklin"],
        "answer": "C",
        "answer_text": "Alexander Graham Bell"
    },

    {
        "question": "What is the hardest natural substance on Earth?",
        "options": ["A) Gold", "B) Iron", "C) Diamond", "D) Quartz"],
        "answer": "C",
        "answer_text": "Diamond"
    },

    {
        "question": "Which country has won the most FIFA World Cups?",
        "options": ["A) Germany", "B) Italy", "C) Argentina", "D) Brazil"],
        "answer": "D",
        "answer_text": "Brazil"
    }
]

print("\n--- Welcome to the QUIZ! ---")
print("--------------------------------------\n")

while True:
    score = 0
    total_questions = len(quiz_data)

    for i, item in enumerate(quiz_data, 1):
        print(f"Q{i}: {item['question']}")

        for opt in item['options']:
            print(opt)

        while True:
            user_ans = input("Answer (A/B/C/D): ").strip().upper()
            
            if user_ans in ['A', 'B', 'C', 'D']:
                break
            print("Invalid entry! Please choose from A, B, C, or D.")

        if user_ans == item['answer']:
            print("\n--> Result: Correct!\n")
            score += 1
        
        else:
            print(f"\n--> Result: Wrong! Correct Answer: {item['answer']}) {item['answer_text']}.\n")

    # Final Result Calculation
    percentage = (score / total_questions) * 100
    print("--------------------------------------")
    print(f"QUIZ COMPLETED!")
    print(f"Your Final Score: {score}/{total_questions} ({percentage:.2f}%)")
    print("--------------------------------------")

    print()
    choice = input("Do you want to play again? (y/n): ").strip().lower()
    print()
    if choice != 'y':
        break