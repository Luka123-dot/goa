# Create a function that takes a list of numbers and then prints the sum of the numbers in that list

def mate():
    list = [1,2,3,5,6,7,7,2,3,5,6,2,4,6,1]
    num = 0
    for i in list:
        num = num + i
    print(num)
mate()