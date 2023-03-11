
num1 = float(input("Enter a number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter a second number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    if num2 == 0:
        print("divide-by-zero error")
    else:
        print(num1 / num2)
else:
    print("incorrect operator")
