#Have the user enter words until he/she enters "stop". Store all words in the list.
list = []
while True:
    bobby = input('enter word here:')
    
    if bobby == 'stop':
        break
    list.append(bobby)
print(list)
    