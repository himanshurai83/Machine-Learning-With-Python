# Create a list of 10 integers and:

# Print the first and last element.

# Print the list in reverse order.

# list1 = list(range(1, 11))
# print(list1)
# print(list1[-1])
# print(list1[0])


# Write a program to find:

# The sum of all elements in a list.

# The maximum and minimum element (without using built-in functions).

# lst = [10, 20, 304, 23, 45]
# print(sum(lst))

# sorted_list = lst.sort()
# print(f"Maximum element {lst[-1]}")
# print(f"Minimum element {lst[0]}")


# Count how many even and odd numbers are in a list.

# lst = [10, 20, 304, 23, 45]
# count = 0
# for i in lst:
#     if i % 2 == 0:
#         count += 1
# print("Even number in the list: ", count)


# Take a list from the user and remove duplicate elements.

# size = int(input("Enter size of the list: "))
# lst = []
# for i in range(0, size):
#     element = int(input("Enter list element: "))
#     lst.append(element)

# unique_element = set(lst)
# print(f"List element are: {list(unique_element)}")


# Check if a given element exists in a list.

# lst = ['mango', 'apple', 'banana']
# if 'mango' in lst:
#     print("Mango is exist..")
# else:
#     print("Mango is not exist..")


# Reverse a list without using reverse() method.

# lst = [10, 20, 30, 40, 50]
# reversed_list = lst[::-1]
# print("Reverse list: ", reversed_list)


# Rotate a list to the right by k positions.
# Example:
# [1,2,3,4,5], k = 2 → [4,5,1,2,3]


# Making list using constructor..
# lst = list(('apple', 'mango', 'kiwi'))
# print(lst)


# Extend

# lst1 = ["apple", "banana", "cherry"]
# lst2 = ["orange", "kiwi", "melon", "mango"]
# lst3 = lst1+lst2
# print(f"Using + operator: {lst3}")
# lst1.extend(lst2)
# print(f"Using extend function: {lst1}")

# lst1 = ["apple", "banana", "cherry"]
# lst2 = ("orange", "kiwi", "melon", "mango")

# lst1.extend(lst2)
# print(lst1)

# Remove
# lst1 = ["orange", "kiwi", "melon", "mango"]
# lst1.remove("orange")
# print(lst1)

# pop
# lst1 = ["apple", "banana", "cherry"]
# lst1.pop(0)
# print(lst1)

# List comprehensive

# list1 = [1, 2, 3, 4, 5]
# new_list = [x**2 for x in list1]
# print(new_list)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# new_list = [x for x in fruits if x.startswith('a')]
# print(new_list)


# lst = [1, 2, 3, 4, 5, 6, 7, 78, 9, 0, 8, 76, 5]
# even = [x for x in range(101) if x % 2 == 0]
# print(even)

# Copy method
# lst1 = [1, 2, 3, 4, 5, 6, 7]
# lst2 = lst1.copy()
# lst2[0] = 10
# print(lst1)
# print(lst2)

# lst1 = [1, 2, 3, 4, 5, 6, 7, 4, 5, 4, 4, 4]
# lst1.reverse()
# print(lst1)
