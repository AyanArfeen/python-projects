# This program greet the user by thier name.

print("Welcome to our Program!!!")
# Take name input
try:
    name = str(input("What your's name?: ")).strip().title()
except ValueError:
    print("Enter only your name.")
    exit()

# Print message
print(f"\nHi, {name}!!\n")