# This program lets the user to play rock-paper-scissors with computer

import random

while True:
    user_choice = input("Type your choice:\n1. Rock\n2. Paper\n3. Scissors:\n--> ").strip().lower()
    if user_choice == '1':
        user_choice = "rock"
    elif user_choice == '2':
        user_choice = "paper"
    elif user_choice == '3':
        user_choice = "scissors"
    else:
        print("Invalid choice!")
        exit()

    computer = random.choice(["rock", "paper", "scissors"])

    print()
    print(f"You choosed {user_choice.capitalize()}! and Computer choosed {computer.capitalize()}!")

    if user_choice == computer:
        print("Draw!")

    elif user_choice == "rock" and computer == "scissors":
        print("--> User win!")

    elif user_choice == "scissors" and computer == "paper":
        print("--> User win!")

    elif user_choice == "paper" and computer == "rock":
        print("--> User win!")

    else:
        print("Computer wins!")

    print()   # Better UI spacing
    choice = input("Do you want to play again? (y/n): ").strip().lower()
    if choice != 'y':
        break
