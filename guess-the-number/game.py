# This program do user to guess the number!

import random

secret = random.randint(1, 10)

try:
    answer = int(input("Enter your guess number between 1 to 10: "))

except:
    print("Please enter number only")
    exit()


if answer == secret:
    print("Correct!")

else:
    print(f"Wrong! The number is {secret}.")