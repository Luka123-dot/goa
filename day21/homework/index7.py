# Create a function that asks the user for a number and then prints whether it is positive or negative

def check_negative_or_Positive():
    num = int(input("Enter a number: "))
    if num < 0:
        print('negative')
    elif num > 0:
        print('positive')
    else:
        print('this is 0')
check_negative_or_Positive()