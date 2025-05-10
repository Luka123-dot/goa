#Write a function that takes a list of strings and returns only the strings that begin with the letter "A".

def if_a(gal):
    for i in gal:
        if i[0] == 'A':
            print(i)
if_a(["Apple", "Banana", "Avocado", "Orange"])

