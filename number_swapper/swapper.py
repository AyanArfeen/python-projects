# This program swaps two numbers without using a temporary variable

while True:
    print("\nThis program lets you swap two numbers.")

    # Take input of numbers
    try:
        a = int(input("Type your first number: "))
        b = int(input("Type your second number: "))
        method = int(input("Choose swap method:\n1. Arithmetic (no temp variable)\n2. Pythonic (tuple unpacking)\n--> "))
    
    except ValueError:
        print("Please enter only Numbers!!")
        continue

    print(f"\nBefore swapping: a = {a}, b = {b}\n")
    
    def swap_numbers(a, b, method=1):
        if method == 1:
            # Swap logic (arithmetic method)
            a = a + b
            b = a - b
            a = a - b

        else:
            a, b = b, a
        
        return a, b
    
    a, b = swap_numbers(a, b, method)

    print("-" * 40)
    print(f"After swapping: a = {a}, b = {b}")
    print("-" * 40)

    choice = input("\nDo you want to swap again? (y/n): ").lower()

    if choice != 'y':
        break
    else:
        continue