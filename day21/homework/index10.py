# Create a function that Asks for a number and then prints all even numbers from one to that number

def one_to_number():
    num = int(input('enter number here:'))
    for i in range(1, num + 1):
        if i % 2 == 0:
            print(i)
one_to_number()