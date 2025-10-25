# This Program will convert Celsius to Fahrenheit and Fahrenheit to Celsius using simple formula

while True:
    print("\nWelcome to our Program")

    a = input("Which conversion you want (C or F) or Enter 'q' to exit: ").lower()
    if a == 'q':
        break
    else:
        pass
    try:
        b = float(input("Give your input(e.g. 12.0): "))
    except ValueError:
        print("Enter only 'number'")
        continue
    result = None


    if a in ['c','celsius']:
        result = (b * 9/5) + 32

    elif a in ['f', 'fahrenheit']:
        result = (b - 32) * 5/9

    else:
        print("--> Enter only C or F Value!")
        continue

    print("-" * 40)
    print(f"---> {b}°{a.upper()} = {result:.2f}°{'F' if a in ['c','celsius'] else 'C'}")
    print("-" * 40)