import numpy as np  

# problem 1
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
sum = a + b
print(f"Sum 1: {sum}")
diff = a - b
print(f"Difference 1: {diff}")

# problem 2
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
sum = a + b
print(f"Sum 2: {sum}")
diff = a - b
print(f"Difference 2: {diff}")

# problem 3
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
dotproduct = np.dot(a, b)
print(f"Dot product 3: {dotproduct}")

# problem 4
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18]])
product = np.dot(a, b)
print(f"Product 4: {product}")

# problem 5
a = np.array([1, 1, 2])
magnitude = np.linalg.norm(a)
print(f"Magnitude 5: {magnitude}")

# problem 6
a = np.array([[1, 2], [3, 4]])
transpose = a.T
print(f"Transpose 6: {transpose}")