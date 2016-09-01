# coding=utf-8
'''
@Title: File Input and Output with Arrays

@Author: tyee.noprom@qq.com
@Time: 9/1/16 10:59 AM
'''

import numpy as np

# Storing Arrays on Disk in Binary Format

arr = np.arange(10)
np.save('some_arr', arr)
arr2 = np.load('some_arr.npy')
np.savez('array_archive.npz', a=arr, b=arr2)
arch = np.load('array_archive.npz')
arch['b']

# Saving and Loading Text Files
phone = np.loadtxt('../data/ch04/phone.txt', delimiter=',', dtype=np.string_)
phone