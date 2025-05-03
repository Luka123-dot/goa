# 9) Print numbers divisible by 4 from 1 to 10
list = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(list)):
    if list[i] % 4 == 0:
        print(list[i])