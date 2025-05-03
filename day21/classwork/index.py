#Create a list and use a for loop to get all even and negative numbers.

list = [-1,-3,4,-4,-6,6,2,-34,4,4,6,4,2,-4,5,5,-3,4,-5,5]

for i in list:
    if i % 2 == 0 and i < 0: #< is naklebis nishani > is metobis nishani.
        print(i)
        
    