# coding=utf-8
'''
@Title:US Baby Names 1880-2010

@Author: tyee.noprom@qq.com
@Time: 8/29/16 6:27 AM
'''

import pandas as pd

data_path = '../data/names/'
names1880 = pd.read_csv(data_path + 'yob1880.txt', names=['name', 'sex', 'births'])
print names1880[:5]
