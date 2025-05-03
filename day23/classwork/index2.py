#Create a function that will have two parameters and this function should multiply these two numbers by each other and then print the remainder, whether it is positive or negative, along with the product. Call this function several times and pass arguments (input and output numbers).

def subtracting_parameters(mate,gochi):
    print(mate * gochi)
    if mate * gochi > 0:
        print('positive')
    elif mate * gochi < 0:
        print('negative')
    elif mate * gochi == 0:
        print('this is a zero try again please.')
subtracting_parameters(5,-4)
subtracting_parameters(-3,2)
subtracting_parameters(23,42)
subtracting_parameters(62,-32)
subtracting_parameters(74,32)
subtracting_parameters(-3,3)
subtracting_parameters(5,5)
subtracting_parameters(134,-12)
    