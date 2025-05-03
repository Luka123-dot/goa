#2)Have the user enter a number, then find the sum of all even numbers up to that number and display the result.
b = 0

num = int(input('enter your number:'))

for h in range(0,num,2):
    b += h
    print(b)
print(b)
