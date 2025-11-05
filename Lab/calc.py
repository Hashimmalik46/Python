print("Simple Calculator")
print("Operations: +, -, *, /, %")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator: ")

if op == '+':
    print("Result:", a + b)
elif op == '-':
    print("Result:", a - b)
elif op == '*':
    print("Result:", a * b)
elif op == '/':
    if b != 0:
        print("Result:", a / b)
    else:
        print("Division by zero not allowed")
elif op == '%':
    print("Result:", a % b)
else:
    print("Invalid operator!")
