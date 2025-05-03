#Write a program that asks the user to enter a number n and calculates the sum of all numbers from 1 to n.  

n = int(input('enter number here:'))
m = 0
for i in range (1,n + 1):
    m += i
print(m)

    