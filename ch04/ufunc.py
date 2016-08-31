# coding=utf-8
'''
@Title: Universal Functions: Fast Element-wise Array Functions

@Author: tyee.noprom@qq.com
@Time: 9/1/16 6:22 AM
'''

import numpy as np

arr = np.arange(10)
np.sqrt(arr)
np.exp(arr)

x = np.random.randn(8)
y = np.random.randn(8)
np.maximum(x, y) # element-wise maximum

arr = np.random.randn(7) * 5
np.modf(arr)