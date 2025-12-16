# This program tells user thier password strength

print("This program tell your Password strength!")
while True:
    user_pass = input("Enter your Password: ").strip()
    if not user_pass:
        print("--> Please enter your password again!!!\n")
        continue

    rules = 0
    strength = None

    if len(user_pass) >= 8:
        rules += 1
    
    if any(char.isdigit() for char in user_pass):
        rules += 1

    if any(char.isupper() for char in user_pass):
        rules += 1

    if any(char.islower() for char in user_pass):
        rules += 1

    if any(not char.isalnum() for char in user_pass):
        rules += 1

    if rules <= 2:
        strength = 'Weak'
    
    elif 2 < rules <= 4:
        strength = 'Medium'
    
    else:
        strength = 'Strong'

    print(f"\nPassword Strength: {strength}!")

    print()
    choice = input("Do you want to play again? (y/n): ").strip().lower()
    print()
    if choice != 'y':
        break