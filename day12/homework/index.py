# 1) Extract from string "ABCDEFGHIJKLMN"
text = "ABCDEFGHIJKLMN"

# 1) "GHIJK"
extract_1 = text[6:11]
print("1) GHIJK: " + extract_1)

# 2) "ACEG"
extract_2 = text[0:13:2]
print("2) ACEG: " + extract_2)

# 3) "NMLKJ"
extract_3 = text[-1:-6:-1]
print("3) NMLKJ: " + extract_3)


# 2) Working with the list of numbers
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# 1) Fifth element (index 4)
fifth_element = numbers[4]
print("1) Fifth element: " + str(fifth_element))

# 2) Reverse the list using slicing
reversed_list = numbers[::-1]
print("2) Reversed list: " + str(reversed_list))


# 3) Shuffle an empty list and manipulate
numbers = []  # Start with an empty list

# Add 5, 10, 15, 20
numbers.extend([5, 10, 15, 20])
print("After adding 5, 10, 15, 20: " + str(numbers))

# Remove the first element by index
numbers.pop(0)
print("After removing the first element: " + str(numbers))

# Remove the number 15
numbers.remove(15)
print("After removing 15: " + str(numbers))

# Check the length
list_length = len(numbers)
print("Length of the list: " + str(list_length))


# 4) Manipulating the list of fruits
fruits = ["apple", "banana", "cherry"]

# 1) Add "orange" and "grape"
fruits.extend(["orange", "grape"])
print("After adding 'orange' and 'grape': " + str(fruits))

# 2) Remove "banana"
fruits.remove("banana")
print("After removing 'banana': " + str(fruits))

# 3) Print the length of the list
fruits_length = len(fruits)
print("Length of the fruits list: " + str(fruits_length))