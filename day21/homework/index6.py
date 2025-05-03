#Create a function that asks the user for a number and then prints whether the number is even or odd


def check_even_or_odd():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print('even')
    else:
        print('odd')
check_even_or_odd()