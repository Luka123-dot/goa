# 7) Print numbers divisible by 3 up to a user input number

num = int(input('enter number here:'))
for i in range(1, num+1 ):
    if i % 3 == 0:
        print(i)
    
