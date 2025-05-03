#Write a program that prints the numbers from 1 to 20 and labels them as "even" or "odd".

for i in range(1,20):
    if i % 2 == 0:
        print(i, 'even')
    else:
        print(i, 'odd')