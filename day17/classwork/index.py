#1)Write a Python program that asks the user to enter a number n and then prints the multiples of n from 1 to 100.
n = int(input('enter numbers here:'))
for i in range(1,100):
    if i % n == 0:
        print(i)