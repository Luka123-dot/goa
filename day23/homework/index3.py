#Ask the user for two numbers then create a function that will have two parameters that will be passed as arguments the user's entered numbers and then print their product

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))


def multiply(x, y):
    print("The product is", x * y)

multiply(a, b)