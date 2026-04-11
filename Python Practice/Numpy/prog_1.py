import numpy as np

arr = np.zeros(5)
print(arr)

arr = np.ones(5)
print(arr)

arr = np.full(5, 7)
print(arr)

arr = np.eye(4)
print(arr)

arr = np.arange(1, 11, 1)
print(arr)
arr_1d = np.array([10, 20, 30, 40, 50])
print(arr_1d)

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d.shape)

arr_3d = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
print(arr_3d.shape)
