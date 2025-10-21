# "This simple program tells your exact age."

try:
    birth_year = int(input("Enter your age (In Number Like 2008): "))
    current_year = int(input("Enter current Year: "))
except ValueError:
    print("Try Again!!")

age = current_year - birth_year

if birth_year >= current_year:
    print("You put a wrong Birth date!")

else:
    print(f"\nYou're {age} years old.\n")