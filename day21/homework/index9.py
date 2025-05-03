#Create a function that asks the user for a number and then prints all the numbers from one to that number

def one_to_number():
    num = int(input('enter number here:'))
    for i in range(1, num + 1):
        print(i)
one_to_number()