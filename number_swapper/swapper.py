# This program swaps two numbers without using a temporary variable

while True:
    print("\nThis program let you swap numbers.")

    # Take input of numbers
    try:
        a = int(input("Type your first number: "))
        b = int(input("Type your second number: "))
    
    except ValueError:
        print("Please enter only Numbers!!")
        continue

    print(f"\nBefore swapping: a = {a:.2f}, b = {b:.2f}")
    
    # Swap logic (arithmetic method)
    a = a + b
    b = a - b
    a = a - b

    print(f"After swapping: a = {a}, b = {b}")

    choice = input("\nDo you want to swap again? (y/n): ").lower()

    if choice != 'y':
        break
    else:
        continue