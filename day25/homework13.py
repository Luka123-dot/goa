#Given a list of numbers. If the number is greater than 5, add it to the new list. (if and append).

list = [1,2,3,4,5,6,7,8,9,10]
list2 = []

for i in list:
    if i > 5:
        list2.append(i)
print(list2)