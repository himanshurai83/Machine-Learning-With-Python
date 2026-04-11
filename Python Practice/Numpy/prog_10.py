import numpy as np

# arr = np.array([10, 25, 30, 45, 50])
# arr[arr > 30] = 0
# print(arr)
arr = np.array([10, 20, 30])
norm = (arr - arr.min()) / (arr.max() - arr.min())
print(norm)
