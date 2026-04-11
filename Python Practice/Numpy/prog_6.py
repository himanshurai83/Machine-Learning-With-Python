import numpy as np

# arr = np.arange(1, 13)
# print(arr)
# print("After Reshape: 3x4")
# new_arr = arr.reshape(3, 4)
# print(new_arr)

# print("After Reshape: 4x3")
# new_arr_2 = new_arr.reshape(4, 3)
# print(new_arr_2)

# way  - 1
# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(arr)
# size = arr.size
# new_arr = arr.reshape(size)
# print(new_arr)


# way - 2
# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# new_arr_2 = arr.ravel()
# print(new_arr_2)

# Insertion(1D)

# arr = np.arange(1, 11)
# print(arr)
# new_arr = np.insert(arr, 3, 5)
# print(new_arr)

# Insertion(2D)

# arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(arr_2d)
# new_arr_2d = np.insert(arr_2d, 1, [10, 20, 30], axis=1)
# print(new_arr_2d)

# Append
# arr = np.arange(1, 11)
# print(arr)
# new_arr = np.append(arr, 100)
# print(new_arr)


# concatenate

arr_1 = np.arange(1, 11)
arr_2 = np.arange(11, 21)
new_arr = np.concatenate((arr_1, arr_2))
print(new_arr)
