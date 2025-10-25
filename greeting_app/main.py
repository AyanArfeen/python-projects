# This program greet the user by thier name.
from datetime import datetime
from random import choice

while True:
    print("Welcome to our Program!!!")

    # Take name input
    name = str(input("What's your name? or Type 'q' to exit: ")).strip().title()
    if name.lower() == 'q':
        break

    if not name: # Checks empty variable
        print("Enter your name please.\n")
        continue

    elif any(ch.isdigit() for ch in name): # Check numbers in name
        print("Names don't contain numbers!\n")
        continue

    greetings = ['Hi', 'Hello', 'Hey', 'Yo', 'Welcome', 'Greetings'] # Added a list of Greetings
    final_greets = choice(greetings) # Randomly chose a greet word

    time = datetime.now().hour
    if time < 12:
        time_of_day = "Morning"
    
    elif time < 18:
        time_of_day = "Afternoon"
    
    else:
        time_of_day = "Evening"

    # Print message
    print()
    print("-" * 30)
    print(f"{final_greets}, {name}! It's a nice {time_of_day}")
    print("-" * 30)
    print()