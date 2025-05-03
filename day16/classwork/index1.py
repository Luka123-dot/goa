#2)Create an empty list, then let the user add numbers and check whether these numbers are positive or negative, and when it returns a positive number, label it positive and a negative number as negative.

list = []


for i in range(5):
    num = int(input('enter number here:'))
    list.append(num)
for i in range(len(list)):
 
    if list[i] >= 0: #[i] = საიტერაციო ცვლადი
        print(list[i], 'positive')
    elif list[i] < 0:
        print(list[i], 'negative')

