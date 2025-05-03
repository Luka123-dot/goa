#Create an empty list, then let the user add numbers and check if these numbers are even or odd, and when they come up with an even number, label them even and odd numbers odd. 


list = []

for i in range(5):
    num = int(input('enter number here:'))

    list.append(num)

for i in range(len(list)):
    if list[i] % 2 == 0 :
        print(list[i], "even")
    elif list[i] % 2 != 0:
        print(list[i], "odd")
    

    
    #odd = კენტი cant be divided by 2, even = ლუწი can be divided by 2

