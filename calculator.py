num1 = float(input("Enter Your 1st Number : "))
num2 = float(input("Enter your 2nd Number :"))

operation = input("Enter your operations (+ , - , * , / , )").strip()

if operation == "+":
    result = num1 + num2

elif operation == "-":
    result = num1 - num2

elif operation == "*":
    result = num1 * num2

elif operation == "/":
        if num2 != 0:
            result = num1 / num2 
        else :
            rersult = "Error! Division by zero"
else :
     result = "Invalid Operation"

print("Result :", result)

