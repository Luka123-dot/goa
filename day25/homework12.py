#Given two lists: ['apple', 'banana', 'cherry'] and ['banana', 'kiwi', 'cherry']. Find which elements are repeated in the second (intersection).


fruit = ['apple','banana', 'cherry']
fruit2 = ['banana', 'kiwi', 'cherry']

for i in fruit:
    if i in fruit2:
        print(i)