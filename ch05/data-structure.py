# coding=utf-8
'''
@Title: Introduction to pandas Data Structures

@Author: tyee.noprom@qq.com
@Time: 9/1/16 5:42 PM
'''
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

obj = Series([4, 7, -5, 3])
obj.values
obj.index

obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
obj2
obj2.index
obj2['a']

obj2[obj2 > 0]
obj2 * 2
np.exp(obj2)

'b' in obj2
'e' in obj2

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = Series(sdata)
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = Series(sdata, index=states)
obj4

pd.isnull(obj4)
pd.notnull(obj4)
obj4.isnull()

obj3 + obj4

obj4.name = 'population'
obj4.index.name = 'state'

obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
