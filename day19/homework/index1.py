#The program asks for numbers and sums them up until the user enters 0.


while True: 
    num = int(input('enter number here:'))
    if num == 0:
        print(True)
        break
    else:
        print('please retry')

