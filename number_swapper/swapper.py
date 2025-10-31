# This program swaps two numbers without using a temporary variable

while True:
    print("\nThis program lets you swap two numbers.")

    # Take input of numbers
    try:
        a = int(input("Type your first number: "))
        b = int(input("Type your second number: "))
    
    except ValueError:
        print("Please enter only Numbers!!")
        continue

    print(f"\nBefore swapping: a = {a}, b = {b}")
    
    # Swap logic (arithmetic method)
    a = a + b
    b = a - b
    a = a - b

    print("-" * 40)
    print(f"After swapping: a = {a}, b = {b}")
    print("-" * 40)

    choice = input("\nDo you want to swap again? (y/n): ").lower()

    if choice != 'y':
        break
    else:
        continue