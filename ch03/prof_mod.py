# coding=utf-8
'''
@Title:Profiling a Function Line-by-Line

@Author: tyee.noprom@qq.com
@Time: 8/31/16 8:32 AM
'''
from numpy.random import randn


def add_and_sum(x, y):
    added = x + y
    summed = added.sum(axis=1)
    return summed


def call_function():
    x = randn(1000, 1000)
    y = randn(1000, 1000)
    return add_and_sum(x, y)
