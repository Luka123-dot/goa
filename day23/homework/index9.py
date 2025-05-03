#Ask the user for a number, then create a function that will have a parameter that will be passed as an argument the number entered by the user, and then print all even numbers from one to that number

num = int(input("Enter a number: "))

def check_even_or_not(n):
    for i in range(1,num + 1):
        if i % 2 == 0:
            print(i)
check_even_or_not(num)