#Write a program that asks the user to enter the word "hello" and does not exit the loop until the user enters exactly that word.

h = 'hello'

while True:
    inp = input('enter word here:')

    if inp == h:
        print('sucess')
        break
    else:
        print('retry')