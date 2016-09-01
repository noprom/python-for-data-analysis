# coding=utf-8
'''
@Title: Linear Algebra

@Author: tyee.noprom@qq.com
@Time: 9/1/16 11:17 AM
'''
import numpy as np
from numpy.linalg import inv, qr

x = np.array([[1., 2., 3.], [4., 5., 6.]])
y = np.array([[6., 23.], [-1, 7], [8, 9]])
x.dot(y)  # equivalently np.dot(x, y)
np.dot(x, np.ones(3))

X = np.random.randn(5, 5)
mat = X.T.dot(X)
inv(mat)