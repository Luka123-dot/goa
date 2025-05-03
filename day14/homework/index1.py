n = int(input("Enter a number: "))


sum_numbers = 0
for i in range(1, n + 1):
    sum_numbers += i


mean = sum_numbers / n


print("The arithmetic mean of numbers from 1 to", n, "is:", mean)