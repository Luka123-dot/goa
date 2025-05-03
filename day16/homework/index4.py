# 4) print only even numbers from the 5 user inputs
list = []

for num in range(5):
    maple = int(input('enter numbers here:'))
    list.append(maple)

for i in range(len(list)):

    if list[i] % 2 == 0:
        print(list[i], 'even')
    

