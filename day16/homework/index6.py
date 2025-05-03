# 6) Count how many of 5 entered numbers are positive
list = []

for i in range(5):
    mate = int(input('enter numbers here:'))
    list.append(mate)

for i in range(len(list)):

    if list[i] >= 0:
        print(list[i], 'positive')


        