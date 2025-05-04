#Given a list ['a', 'b', 'c', 'd', 'e']. Delete all elements whose index is even (0,2,4...).

list = ['a', 'b', 'c', 'd', 'e']
broski = []
for i in range(len(list)):
    if i % 2 != 0:
        broski.append(list[i])
print(broski)
    