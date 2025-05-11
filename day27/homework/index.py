#Write a function that asks the user for a number and adds it to a list if it is not in the list.

def add_number(bra):
    for i in bra:
        num = int(input('enter number here:'))
        if num not in bra:
            bra.append(num)
add_number(1,4,5,2,5)