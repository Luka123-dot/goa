#Write a function that returns true if a number is greater than 10:

def true_if_10():
    num = int(input('enter number here:'))
    if num > 10:
        print(True)
    elif num < 10:
        print(False)
    elif num == 10:
        print(False)
true_if_10()