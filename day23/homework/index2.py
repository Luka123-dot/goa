# Ask the user for two numbers then create a function that will have two parameters that will be passed as arguments the user's entered numbers and then subtract them

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))


def subtract(x, y):
    print("The sum is", x - y)

subtract(a, b)