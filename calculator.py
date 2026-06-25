num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))
result = float(0)

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Cannot divide by zero. If you could the Universe would probably Blue Screen")
        exit() 

print(f"Result: {result}")
