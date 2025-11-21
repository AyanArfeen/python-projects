# This program lets the user guess the number!

import random

while True:
    secret = random.randint(1, 10)

    print()  # UI spacing
    user_input = input("Enter your guess number between 1 to 10 or type 'q' to exit: ").strip().lower()
    
    if user_input == 'q':
        print("Thanks for playing the game.")
        break

    try:
        guess = int(user_input)
    except ValueError:
        print("Invalid Input! Please enter a number between 1 to 10.\n")
        # No play-again question here—just restart cleanly
        continue

    if guess == secret:
        print("Correct!")
    else:
        print(f"Wrong! The number is {secret}.")

    print()   # Better UI spacing
    choice = input("Do you want to play again? (y/n): ").strip().lower()
    if choice != 'y':
        break
