import numpy as np

# arr1 = np.array([1, 2, 3, 4, 5, 6])
# print(arr1)

# arr2 = np.empty((2, 2))
# print(arr2)

# arr3 = np.arange(1, 11, 2)
# print(arr3)

# arr4 = np.linspace(1, 10, 5)
# print(arr4)

# arr5 = np.logspace(1, 10, 5)
# print(arr5)

# arr6 = np.eye(3)
# print(arr6)

# arr7 = np.full((2, 2), 7)
# print(arr7)


# a = np.arange(1, 10)
# b = a.reshape((3, 3))
# print(np.shape(a))
# print(b)
# print(np.shape(b))

# n = int(input("Enter the last term: "))
# a = np.arange(1, n+1)
# print(f"The sum of first {n} number is {np.sum(a)}")
# print(f"The mean of first {n} number is {np.mean(a)}")
# print(f"The minimum element is {np.min(a)}")
# print(f"The maximum element is {np.max(a)}")
# print(f"The standard deviation of first {n} number is {np.std(a)}")
# print(f"The variance of first {n} number is {np.var(a)}")
# print(f"The sqrt of first {n} number is {np.sqrt(a)}")
# print(f"The Square of first {n} number is {np.power(a, 2)}")

# arr8 = np.where(a > 5)
# print(arr8)

# arr8 = np.where(a > 5, "High", "Low")
# print(arr8)

arr9 = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr9)
arr10 = np.array([[1, 2], [4, 5]])
# print(arr10)
# print(arr9 + arr10)

# print(np.dot(arr10, arr9))
# print(np.matmul(arr10, arr9))

# print(np.linalg.inv(arr10))
print(np.linalg.det(arr10))
