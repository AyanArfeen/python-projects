# Quiz Game

quiz_data = [
    {
        "question": "Which planet is known as the 'Red Planet'?",
        "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "B"
    },

    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
        "answer": "D"
    },

    {
        "question": "Who is credited with inventing the telephone?",
        "options": ["A) Thomas Edison", "B) Nikola Tesla", "C) Alexander Graham Bell", "D) Benjamin Franklin"],
        "answer": "C"
    },

    {
        "question": "What is the hardest natural substance on Earth?",
        "options": ["A) Gold", "B) Iron", "C) Diamond", "D) Quartz"],
        "answer": "C"
    },

    {
        "question": "Which country has won the most FIFA World Cups?",
        "options": ["A) Germany", "B) Italy", "C) Argentina", "D) Brazil"],
        "answer": "D"
    }
]

print("\nWelcome to QUIZ!\n")

score = 0

for i, item in enumerate(quiz_data, 1):
    print(f"Q{i}: {item['question']}")

    for opt in item['options']:
        print(opt)

    user_ans = input("Answer (A/B/C/D): ").strip().upper()

    if user_ans == item['answer']:
        print("\n--> Correct Answer\n")
        score += 1
    
    else:
        print(f"\n--> Wrong! Correct Answer is {item['answer']}.\n")

print(f"Your scored {score} out of {i}.")