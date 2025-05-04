#Ask the user to enter 5 words, add them to the list and print the list sorted alphabetically (sort).

list = []

for i in range(5):
    bru = input('enter words here:')
    list.append(bru)
list.sort()
print(list)

