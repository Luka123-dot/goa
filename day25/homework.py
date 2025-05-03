# # 1. Create an empty list and add 5 of your favorite foods to it
# foods = []
# foods.extend(["pizza", "sushi", "burger", "fries", "pasta"])

# # 2. Add 'orange' to list
# fruits = ['apple', 'banana', 'cherry']
# fruits.append('orange')

# # 3. Remove the first element from a list
# numbers = [5, 10, 15]
# numbers.pop(0)

# # 4. Remove 'cat' using remove method
# animals = ['dog', 'cat', 'bird']
# animals.remove('cat')

# # 5. Count the number of elements in a list
# print("Number of elements:", len(foods))

# # 6. Print only the variable numbers (odd numbers)
# nums = [1, 2, 3, 4, 5]
# for num in nums:
#     if num % 2 == 0:
#         print("Odd number:", num)

# # 7. Ask user to enter 5 numbers and write to list
# user_nums = []
# for i in range(5):
#     user_input = int(input("Enter number: "))
#     user_nums.append(user_input)

# # 8. Remove last element using pop and print it
# even_list = [2, 4, 6, 8, 10]
# removed = even_list.pop()
# print("Removed element:", removed)

# # 9. Move all even numbers to a new list
# mixed_nums = [1, 2, 3, 4, 5, 6]
# even_nums = []
# for i in mixed_nums:
#     if i % 2 == 0:
#         even_nums.append(i)
# print(even_nums)
    
    


# # 10. Delete all elements from a list
# clear_list = [1, 2, 3]
# clear_list.clear()

# 11. Ask user to enter 5 words, add to list and sort
words = []
ka = input('enter word here:')
for i in range(5):
    

# 12. Find repeated elements (intersection)
list1 = ['apple', 'banana', 'cherry']
list2 = ['banana', 'kiwi', 'cherry']

# 13. Numbers > 5 to a new list
sample_nums = [2, 6, 9, 1, 5, 10]


# 14. Ask user to enter several numbers, then print the largest
user_inputs = []

  

# 15. Delete elements with even index
letters = ['a', 'b', 'c', 'd', 'e']


# 16. Merge two lists
list_a = [1, 2, 3]
list_b = [4, 5, 6]
merged = list_a + list_b

# 17. Enter words until "stop"
user_words = []
while True:
    word = input("Enter a word (type 'stop' to finish): ")
    if word.lower() == 'stop':
        break
    user_words.append(word)
print("Words entered:", user_words)

# 18. Remove duplicates from list
nums = [1, 2, 2, 3, 4, 4, 5]
unique = []

for n in nums:
    is_duplicate = False
    for i in unique:
        if n == i:
            is_duplicate = True
            break
    if is_duplicate == False:
        unique.append(n)

print(unique)

# 19. Find common elements of two lists
a = [1, 2, 3]
b = [2, 3, 4]
common = []

for x in a:
    if x in b:
        common.append(x)

print(common)

# 20. Multiply each number by 2
nums = [1, 2, 3]
doubled = []

for n in nums:
    doubled.append(n * 2)

print(doubled)