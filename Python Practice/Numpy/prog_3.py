import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [
               16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])
# print(arr)
print(f"Dimension: {arr.ndim}")
print(f"Type: {arr.dtype}")
print(f"Shape: {arr.shape}")

# slicing
# Fetching only one row
print(arr[0:1])
# Fetching last row
print(arr[0:5, 4])
# middle 3x3 matrix
print(arr[1:4, 1:4])

# Fancy Indexing
arr = np.array([1, 203, 4, 50, 6, 7, 806, 404, 302, 23, 23, 4, 4534, 5, 456])
print(arr[[0, 2, 4]])

# Boolean Masking
arr = np.array([1, 203, 4, 50, 6, 7, 806, 404, 302, 23, 23, 4, 4534, 5, 456])
print(arr[arr > 25])
