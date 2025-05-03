#Ask the user for a number then create a function that will have a parameter that will be passed as arguments the user's entered numbers and then Yes, it will print whether this number is even or odd

num = int(input("Enter a number: "))

def check_even_odd(n):
    if n % 2 == 0:
        print("Yes, the number is even.")
    else:
        print("No, the number is odd.")

check_even_odd(num)
