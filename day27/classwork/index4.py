#Write a function that takes a list of strings and returns only those strings whose length is greater than 4.

def check_strings(blo):
    for i in blo:
        if len(i) > 4:
            print(i)
check_strings(["cat", "banana", "hat", "window"])