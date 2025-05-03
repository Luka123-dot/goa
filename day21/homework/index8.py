#Create a function that asks the user for their age and if their age is greater than 18, tells them whether they are an adult or not

def adult_or_not():
    adult = float(input('enter age here:'))
    if adult >= 18:
        print('adult')
    elif adult < 18:
        print('not adult')
adult_or_not()
