# coding=utf-8
'''
@Title: The numpy array

@Author: tyee.noprom@qq.com
@Time: 8/31/16 6:37 PM
'''

import numpy as np

data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)

data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)

np.zeros(10)
np.zeros((3, 6))
np.empty((2, 3, 6))
np.arange(15)

arr3 = np.array([1, 2, 3], dtype=np.float64)
arr4 = np.array([1, 2, 3], dtype=np.int32)

# dtype convert
arr = np.array([1, 2, 3, 4, 5])
arr.dtype
float_arr = arr.astype(np.float64)
float_arr.dtype

# float to int
arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
arr.astype(np.int32)

numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
numeric_strings.astype(float)

int_array = np.arange(10)
calibers = np.array([.22, .270, .357, .380, .44, .50], dtype=np.float64)
int_array.astype(calibers.dtype)

empty_uint32 = np.empty(8, dtype='u4')
empty_uint32
