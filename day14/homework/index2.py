# Let the user enter a number and then print the sum of all the numbers of the squared from one to this number.


num = int(input('enter number here:'))

gochi = 0

for i in range(num):
    gochi += (i * i)

print(num)