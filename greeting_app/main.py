# This program greet the user by thier name.

print("Welcome to our Program!!!")
# Take name input
name = str(input("What's your name?: ")).strip().title()

if not name: #Checks empty variable
    print("Enter your name please.")

elif any(ch.isdigit() for ch in name): # Check numbers in name
    print("Names don't contain numbers!")

else:
    # Print message
    print("-" * 30)
    print(f"Hi, {name}!!")
    print("-" * 30)