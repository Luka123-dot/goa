#Write a program that takes a list and returns a new list with no duplicates (unique values).

broken = [1,2,2,3,4,5,6,2]
mroken = []

for i in broken:
    if i not in mroken:
        mroken.append(i)
print(mroken)