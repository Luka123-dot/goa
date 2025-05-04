#Write a program that finds the common elements of two lists and stores the result in a new list.

microsoftstore = [1,2,3,4,5,6]
microsoftstore2 = [1,2,4,7,2,5]
microsoftstore3 = []

for i in microsoftstore:
    if i in microsoftstore2 and i not in microsoftstore3:
        microsoftstore3.append(i)
print(microsoftstore3)