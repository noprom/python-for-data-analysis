# coding=utf-8
'''
@Title:US Baby Names 1880-2010

@Author: tyee.noprom@qq.com
@Time: 8/29/16 6:27 AM
'''

import pandas as pd
import numpy as np
import matplotlib as plt

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
# print names.describe

# pivot_table operation
total_births = pd.pivot_table(names, index='year', values='births', columns='sex', aggfunc=np.sum)
print total_births.tail()
# TODO
total_births.plot(title='Total births by sex and year')


def add_prop(group):
    # Integer division floors
    births = group.births.astype(float)
    group['prop'] = births / births.sum()
    return group


names = names.groupby(['year', 'sex']).apply(add_prop)
print names.head()

# use np.allclose to check that the group sums are sufficiently close to (but perhaps not exactly equal to) 1:
print np.allclose(names.groupby(['year', 'sex']).prop.sum(), 1)


def get_top1000(group):
    return group.sort_values(by='births', ascending=False)[:1000]


grouped = names.groupby(['year', 'sex'])
top1000 = grouped.apply(get_top1000)
print top1000