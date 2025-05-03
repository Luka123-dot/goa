#Create a list then let the user add 1 item then remove 1 item and remove 1 item by index


list = [1,2,3,4,5,6,7,8,9,10]

num1 = int(input("please enter the number here:"))

list.append(num1)

print(list)

num2 = int(input('please enter the number here:'))

list.remove(num2)

print(list)

num3 = int(input('input the number here:'))

list.pop(num3)

print(list)