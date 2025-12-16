# This program tells user thier password strength

print("This program tells your password strength!")
while True:
    user_pass = input("Enter your Password: ").strip()
    if not user_pass:
        print("--> Please enter your password again!!!\n")
        continue

    issues = []
    strength = None

    if len(user_pass) >= 8:
        pass
    else:
        issues.append("Password must be at least 8 characters")
    
    if any(char.isdigit() for char in user_pass):
        pass
    else:
        issues.append("No digit found")

    if any(char.isupper() for char in user_pass):
        pass
    else:
        issues.append("No uppercase letter")

    if any(char.islower() for char in user_pass):
        pass
    else:
        issues.append("No lowercase letter")

    if any(not char.isalnum() for char in user_pass):
        pass
    else:
        issues.append("No special character")

    if len(issues) >= 3:
        strength = 'Weak'
    
    elif len(issues) == 1 or len(issues) == 2:
        strength = 'Medium'
    
    elif len(issues) == 0:
        strength = 'Strong'

    print(f"\nPassword Strength: {strength}")
    
    if len(issues) == 0:
        print("- No Issues")
    
    else:
        print("Issues:")
        for issue in issues:
            print(f"- {issue}")

    print()
    choice = input("Do you want to play again? (y/n): ").strip().lower()
    print()
    if choice != 'y':
        break