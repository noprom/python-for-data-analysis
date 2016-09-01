# coding=utf-8
'''
@Title: Mathematical and Statistical Methods

@Author: tyee.noprom@qq.com
@Time: 9/1/16 8:41 AM
'''

import numpy as np

arr = np.random.randn(5, 4)  # normally-distributed data
arr.mean()
np.mean(arr)
arr.sum()
arr.mean(axis=1)
arr.sum(0)

arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
arr.cumsum(0)
arr.cumprod(1)

# Methods for Boolean Arrays
arr = np.random.randn(100)
(arr > 0).sum()  # Number of positive values
bools = np.array([False, False, True, False])
bools.any()
bools.all()

# Sorting
arr = np.random.randn(8)
arr
arr.sort()

arr = np.random.randn(5, 3)
large_arr = np.random.randn(1000)
large_arr.sort()
large_arr[int(0.05 * len(large_arr))]  # 5% quantile

# Unique and Other Set Logic
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
np.unique(names)
ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
np.unique(ints)

values = np.array([6, 0, 0, 3, 2, 5, 6])
np.in1d(values, [2, 3, 6])
