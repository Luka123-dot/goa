#Write a program that prints all even numbers from 1 to n using a while loop.
n = int(input('enter number here:'))
i = 1
while i <= n:
    if i % 2 == 0:
        print(i)

    