#Write a function that takes a list of numbers and returns only positive numbers.

def positive_numbers(list):
    for i in list:
        if i > 0:
            print(i)
        elif i == 0:
            print('this is zero try again')
positive_numbers([3,-4,52,5,3,5,-3.5,345,-4,-5,-5,-6,-3,53,0,4,5])