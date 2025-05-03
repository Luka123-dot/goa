#Let the user enter a number and then print the product of all the numbers from one to this number.


n = int(input("Enter a number: "))


product = 1
for i in range(1, n + 1):
    product *= i


print("The product of numbers from 1 to", n, "is:", product)