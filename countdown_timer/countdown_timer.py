import time
while True:
    while True:
        try:
            second = int(input("Enter seconds: "))

            if second <= 0:
                print("--> Enter a number greater than 0.\n")
            else:
                break

        except ValueError:
            print("--> Invalid! Enter numbers only.\n")

    for i in range(second, -1, -1):
        print(f"Time left: {i} seconds")
        time.sleep(1)

    print("Time’s up!")

    print()
    choice = input("Do you want to create another timer? (y/n): ").strip().lower()
    print()
    if choice != 'y':
        print("Thanks for using the program!")
        break