# This program swaps two numbers without using a third variable

while True:
    print("\nThis program let you swap numbers.")

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

    print(f"After swapping: a = {a}, b = {b}")