#Ask the user for a number, then create a function that will have a parameter that will be passed as an argument the number entered by the user, and then print whether this number is positive or negative

num = int(input("Enter a number: "))

def check_negative_positive(n):
    if n > 0:
        print("Yes, the number is positive.")
    elif n < 0:
        print("No, the number is negative.")
    elif n == 0:
        print('this is zero')

check_negative_positive(num)