operator =  input("Enter an Operator ( + - * /) : ")
num1 = float(input("Enter the 1st Number: "))
num2 = float(input("Enter the 2nd Number : "))

if operator == "+":
    result =  num1 +  num2
    print(round(result))
elif operator == "-":
    result =  num1 - num2
    print(round(result))

elif operator == "*":
    result =  num1 *  num2
    print(round(result))

elif operator == "/":
    result =  num1 / num2
    print(round(result))
