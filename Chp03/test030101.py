import numpy as np          # pip install numpy

# arr = np.array([[1, 2], [3, 4]])

# print("type: {}".format(type(arr)))
# print("shape: {}, dimension: {}, dtype: {}".format(arr.shape, arr.ndim, arr.dtype))
# print("Array's Max: {}, Min: {}, Mean: {}, , Sum: {}".format(arr.max(), arr.min(), arr.mean(), arr.sum()))
# print("Array's Data:\n", arr)
# print("Array's 1st Row: {}, 2nd Row: {}".format(arr[0], arr[1]))
# print("Array's 1st Row's 1st & 2nd Data: {} {}, 2nd Row's 1st & 2nd Data: {} {}".format(arr[0][0], arr[0][1], arr[1][0], arr[1][1]))
# print("Array's 1st Row's 1st & 2nd Data: {} {}, 2nd Row's 1st & 2nd Data: {} {}".format(arr[0, 0], arr[0, 1], arr[1, 0], arr[1, 1]))
# print("Elements bigger than 1 in Array: ", arr[arr>1])
# print("Array's Transpose (T):\n", arr.T)
# print("Array's Transpose (transpose()):\n", arr.transpose())
# print("Array's Flatten:", arr.flatten())

# print("배열의 연산")
# print("Add:\n", arr + arr)
# print("Subtract:\n", arr - arr)
# print("Multiply:\n", arr * arr)
# print("Divide:\n", arr / arr)

A = np.array([[1, 2], [3, 4]])
B = np.array([10, 100])

print("Dot Product1 of A and B:", np.dot(A, B))
print("Dot Product2 of A and B:", A.dot(B))