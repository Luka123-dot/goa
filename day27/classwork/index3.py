#Write a function that takes a list of numbers and returns a list where all numbers are squared, but only if that value is positive.

def square_positive(grass):
    for i in grass:
        if i > 0:
            print('positive', i ** 2)
square_positive([3,-4,52,5,3,5,-3.5,345,-4,-5,-5,-6,-3,53,0,4,5])