import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(arr)
print(f"Dimension: {arr.ndim}")
print(f"Size: {arr.size}")
print(f"Shape: {arr.shape}")
print(f"Data Type: {arr.dtype}")


arr = np.array([30.5, 40, 60, 50.6, 77.7, 90])
print(f"Dimension: {arr.ndim}")
print(f"Data type: {arr.dtype}")
print(arr)
new_arr = arr.astype(int)
print(new_arr)
print(f"Data type: {new_arr.dtype}")
