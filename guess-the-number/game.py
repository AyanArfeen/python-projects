# This program lets the user guess the number!

import random
quit_game = False

while True:
    print()
    difficulty = input("Choose difficulty:\n1. Easy (1-10)\n2. Medium (1-50)\n3. Hard (1-100):\n---> ").strip().lower()
    
    if difficulty in ["1", "easy"]:
        max_range = 10

    elif difficulty in ["2", "medium"]:
        max_range = 50

    elif difficulty in ["3", "hard"]:
        max_range = 100

    else:
        print("Try Again!!")
        continue

    secret = random.randint(1, max_range)
    attempts = 0

    while True:
        print()  # UI spacing
        user_input = input("Enter your guess number according to your chosen difficulty or type 'q' to exit: ").strip().lower()
        
        if user_input == 'q':
            print("Thanks for playing the game.")
            quit_game = True
            break

        try:
            guess = int(user_input)
        except ValueError:
            print("Please enter a valid number!\n")
            # No play-again question here—just restart cleanly
            continue

        attempts += 1
        
        if guess < secret:
            print("Too Low!")
            continue
        
        if guess > secret:
            print("Too High!")
            continue
        
        if guess == secret:
            print(f"You guessed it in {attempts} tries!")
            break

    if quit_game:
        break

    print()   # Better UI spacing
    choice = input("Do you want to play again? (y/n): ").strip().lower()
    if choice != 'y':
        break
