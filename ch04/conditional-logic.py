# coding=utf-8
'''
@Title: Expressing Conditional Logic as Array Operations

@Author: tyee.noprom@qq.com
@Time: 9/1/16 8:07 AM
'''

import numpy as np

xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])

result = [(x if c else y) for x, y, c in zip(xarr, yarr, cond)]

# another concise way
result = np.where(cond, xarr, yarr)
result

arr = np.random.randn(4, 4)
np.where(arr > 0, 2, -2)
np.where(arr > 0, 2, arr)  # set only positive values to 2
