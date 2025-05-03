#Print a pyramid of stars according to the height entered by the user. xample:     

#    *    
#   ***   
#  *****  
# ******* 
#*********

n = int(input('enter number here:'))
for i in range(1,n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
    