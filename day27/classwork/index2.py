#Write a function that takes a list of numbers, finds only even numbers, and multiplies them by two.

def mulyiplying_numbers(kro):
    for i in kro:
        if i % 2 == 0:
            print('even', i * 2)
mulyiplying_numbers([3,-4,52,5,3,5,-3.5,345,-4,-5,-5,-6,-3,53,0,4,5])