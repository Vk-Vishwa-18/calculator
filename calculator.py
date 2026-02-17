num1 = int(input("Enter the first number:"))
num2  = int(input("Enter the second number:"))
operation =input("Enter the operation you want to perform (+, -, *, /):")

if operation == "+":
    print("Result is:",num1+num2)

elif operation =="-":
    print("Result is:",num1-num2)

elif operation =="*":
    print("Result is:",num1*num2)

elif operation =="/":
    if num2 != 0:
        print("Result is:",num1/num2)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter one of +, -, *, /.")