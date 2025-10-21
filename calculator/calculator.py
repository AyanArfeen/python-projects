# Basic Operations Calculator
# This is my first try

a = int(input("Give First Number: "))
b = input("Give '+' '-' '/' '*' to perform calculations: ")
c = int(input("Give Second Number: "))
print("\nCalculation is: ")

# pure logic

if "+" in b:
    print(a + c)

elif "-" in b:
    print(a - c)

elif "/" in b:
    print(a / c)

elif "*" in b:
    print(a * c)

else:
    print("You put a wrong Operation!!")
