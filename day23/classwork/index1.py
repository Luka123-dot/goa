#Create a function that will have two parameters and this function should multiply these two numbers by each other and then print the resulting remainder along with whether the product is even or odd. Call this function several times and pass arguments (numbers).

def subtracting_parameters(mate,gochi):
    print(mate * gochi)
    if mate * gochi % 2 == 0:
        print('even')
    elif mate * gochi % 2 == 1:
        print('odd')
subtracting_parameters(5,4)
subtracting_parameters(3,2)
subtracting_parameters(23,42)
subtracting_parameters(62,32)
subtracting_parameters(74,32)
subtracting_parameters(3,3)
subtracting_parameters(5,5)
subtracting_parameters(134,12)
    