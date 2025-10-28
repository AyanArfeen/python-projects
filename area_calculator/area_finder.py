# This program calculate area of given shapes
import math

while True:
    shape = input("\nWhich shape's area do you want to find?\n1. Circle\n2. Rectangle\n3. Triangle\nOr (type 'q' to quit): ")
    unit = input("Enter unit (Like cm or m): ").strip()
    if shape.lower() == 'q':
        break

    if shape.lower() in ["1", "circle"]:
        try:
            radius = float(input("Enter the Radius: "))

        except ValueError:
            print("Please enter correct values!\n")
            continue
        
        calculations = math.pi * (radius ** 2)

    elif shape.lower() in ["2", "rectangle"]:
        try:
            length = float(input("Enter the Length: "))
            width = float(input("Enter the width: "))
        
        except ValueError:
            print("Please enter correct values!\n")
            continue

        calculations = length * width

    elif shape.lower() in ["3", "triangle"]:
        try:
            base = float(input("Enter the Base: "))
            height = float(input("Enter the Height: "))
        
        except ValueError:
            print("Please enter correct values!\n")
            continue
        
        calculations = 0.5 * base * height

    else:
        print("Please select a correct number!\n")
        continue

    print("-" * 40)
    print(f"The Area is: {calculations:.2f} {unit}²")
    print("-" * 40)