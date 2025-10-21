# This code tell whether a number is even or odd
print("Welcome!! Our program tells whether a number is odd or even. Give it a try\n")
while True:
    try:
        num = int(input("Enter the Number: "))
    except ValueError:
        print("Invalid Input!! Enter only numbers.")
        exit()

    if num % 2 == 0:
        print("Even\n")

    else:
        print("Odd\n")