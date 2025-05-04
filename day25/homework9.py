#Write a program that will move all even numbers from a list to a new list.

list = [1,2,3,4,5,6,7,8]
list1 = []

for i in list:
    if i % 2 == 0:
        list1.append(i)
print(list1)

