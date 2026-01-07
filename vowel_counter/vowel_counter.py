# This program will count number of vowel in a string

print("=" * 30 + "\n\tVowel Counter\n" + "=" * 30)

while True:
    user_input = input("Enter a string: ").strip().lower()

    if not user_input:
        print("You entered an empty string. Please enter a valid string.")
        continue
    
    vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    total_vowels = 0

    for char in user_input:
        if char in vowel_counts:
            vowel_counts[char] += 1
            total_vowels += 1
        
    print(f"\nTotal vowels found: {total_vowels}")

    for vowel, count in vowel_counts.items():
        print(f"'{vowel}': {count}")

    choice = input("\nDo you want to check another string? (y/n): ").strip().lower()
    if choice != 'y':
        print("=" * 30 + "\nThank you for using the Vowels Checker!\n" + "=" * 30)
        break