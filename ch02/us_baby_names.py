# coding=utf-8
'''
@Title:US Baby Names 1880-2010

@Author: tyee.noprom@qq.com
@Time: 8/29/16 6:27 AM
'''

import pandas as pd

data_path = '../data/ch02/names/'
names1880 = pd.read_csv(data_path + 'yob1880.txt', names=['name', 'sex', 'births'])
print names1880[:5]

# we can use the sum of the births column by sex as the total number of births in that year:
print names1880.groupby('sex').births.sum()

# 2010 is the last available year right now
years = range(1880, 2010)
pieces = []
columns = ['name', 'sex', 'births']
for year in years:
    path = data_path + 'yob%d.txt' % year
    frame = pd.read_csv(path, names=columns)
    frame['year'] = year
    pieces.append(frame)

# Concatenate everything into a single DataFrame
names = pd.concat(pieces, ignore_index=True)
print names.describe

# TODO: pivot_table operation
total_births = names.pivot_table('births', rows='year', cols='sex', aggfunc=sum)
total_births.tail()
