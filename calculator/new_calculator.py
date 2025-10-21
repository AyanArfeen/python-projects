#Enhanced version of Calculator

a = float(input("Give First Number: "))
b = input("Give '+' '-' '/' '*' to perform calculations: ")
c = float(input("Give Second Number: "))
result = None

# pure logic

if b == "+":
    result = a + c

elif b == "-":
    result = a - c

elif b == "/":
    if c == 0:
        result = "Error: Division by 0 is not possible"
    else:
        result = a / c

elif b == "*":    
    result = a * c

else:
    result = "Invalid Operation"

print(f"\n--> {a} {b} {c} = {result}")