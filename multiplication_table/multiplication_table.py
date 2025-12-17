# This Program gives the multiplication table of any number!
print("This Program creates a Multiplication table of any given number.")

while True:
    while True:
        try:
            number = int(input("Enter the number: "))
            upto = int(input("Do you want the table up to 10, 20, or another number?: "))

            if number == 0 or upto == 0:
                print("--> The table of 0 is always 0.\n")
                continue
            elif number < 0 or upto < 0:
                print("Negative numbers are not allowed. Try again.\n")
            else:
                break

        except ValueError:
            print("Invalid! Enter numbers only.\n")
            continue

    print(f"\nMultiplication Table for {number}:")
    for i in range(1, (upto+1)):
        print(f"{number} x {i} = {number * i}")

    print("-------------------------")

    print()
    choice = input("Do you want to create another table? (y/n): ").strip().lower()
    print()
    if choice != 'y':
        print("Thanks for using the program!")
        break