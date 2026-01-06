import re # Used to remove special characters

print('='*30)
print("Palindrome Checker Program")
print('='*30 + '\n')

while True:
    user_input = input("Enter a string: ").strip()

    if not user_input:
        print("--> You entered an empty string. Please enter a valid string.")
        continue

    cleaned_str = re.sub(r'[^a-zA-Z0-9]', '', user_input).lower()

    if cleaned_str == cleaned_str[::-1]:
        print("--> It is a palindrome")

    else:
        print("--> Not a palindrome")

    choice = input("\nDo you want to check another string? (y/n): ").strip().lower()
    if choice != 'y':
        print('\n' + '='*30)
        print("Thank you for using the Palindrome Checker!")
        print('='*30)
        break
