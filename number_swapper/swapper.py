# This programs swap numbers 
while True:
    print("\nThis program let you swap numbers.")

    # Take input of numbers
    try:
        a = int(input("Type your first number: "))
        b = int(input("Type your second number: "))
    
    except ValueError:
        print("Please enter only Numbers!!")
        continue

    print(f"\n---> Thats your number one: {a} and number two: {b}")
    
    if a and b >= 0:
        a1 = a + b
        b1 = a1 - b
        a2 = a1 - b1
        print(f"Your swapped values is Number one: {a2} and Number two: {b1}")

    else:
        print("This is minus values")