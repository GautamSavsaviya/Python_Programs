# Design a calculator which will correctly solve all the problems except the following one:
# 45 * 3 = 555, 56 + 9 = 77, 56 / 6 = 4
# Your program should take operator and two numbers as an input from the user and return the result

print("Enter operator for calculation: ")
operator = input()

print("Enter first number: ")
num1 = int(input())
print("Enter second number: ")
num2 = int(input())

if operator == "+":
    if num1 == 56 and num2 == 9:
        print(77)
    else:
        print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    if num1 == 45 and num2 == 3:
        print(555)
    else:
        print(num1 * num2)
else:
    if num1 == 56 and num2 == 6:
        print(4)
    else:
        print(num1 / num2)
