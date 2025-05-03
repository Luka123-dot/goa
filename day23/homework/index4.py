#Ask the user for two numbers then create a function that will have two parameters that will be passed as arguments the user's entered numbers and then print their division

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))


def division(x, y):
    print("The division is", x / y)

division(a, b)