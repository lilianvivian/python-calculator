# a calculator
num1 = int(input("Enter the num1:"))
num2 = int(input("Enter the num2:"))
operation = input("Enter the operation(+,-,*,/):")

if operation == '+':
    result = num1 + num2
    print (f" {num1} + {num2} = {result}")

elif operation == '-':
        result = num1 - num2
        print (f"{num1} - {num2} = {result}")

elif  operation == '*':
    result = num1 * num2
    print (f"{num1} * {num2} = {result}")

elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print (f"{num1} / {num2} = {result}")
    else:
        print("Error! Division by zero is not allowed")
else:
    print ("Invalid")