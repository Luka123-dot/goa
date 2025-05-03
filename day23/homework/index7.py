# Ask the user for a number, then create a function that will have a parameter that will be passed as an argument the number entered by the user, and then tell if he is over 18 or not

num = int(input("Enter a number: "))

def check_adult_or_not(n):
    if n >= 18:
        print("Yes, this person is an adult.")
    else:
        print('not adult')

check_adult_or_not(num)