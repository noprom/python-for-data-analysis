# coding=utf-8
'''
@Title: Operations between Arrays and Scalars

@Author: tyee.noprom@qq.com
@Time: 8/31/16 7:25 PM
'''

import numpy as np

arr = np.array([[1., 2., 3.], [4., 5., 6.]])

a = arr * arr
b = arr - arr
c = 1 / arr
d = arr ** 0.5

arr = np.arange(10)
arr[5]
arr[5:8]
arr[5:8] = 12

arr_slice = arr[5:8]
arr_slice[1] = 12345
arr_slice[:] = 64

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr2d[2]
assert (arr2d[0][2] == arr2d[0, 2])

arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
arr3d[0]
old_values = arr3d[0].copy()
arr3d[0] = 42
arr3d[0] = old_values

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.randn(7, 4)

# Fancy Indexing
arr = np.empty((8, 4))

for i in range(8):
    arr[i] = i

arr = np.arange(32).reshape((8, 4))
arr[[1, 5, 7, 2], [0, 3, 1, 2]]
arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]]

# Transposing Arrays and Swapping Axes
arr = np.arange(15).reshape((3, 5))
arr.T

arr = np.random.randn(6, 3)
np.dot(arr.T, arr)

arr = np.arange(16).reshape((2, 2, 4))
arr.transpose((1, 0, 2))
arr.swapaxes(1, 2)