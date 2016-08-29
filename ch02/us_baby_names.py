# coding=utf-8
'''
@Title:US Baby Names 1880-2010

@Author: tyee.noprom@qq.com
@Time: 8/29/16 6:27 AM
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

# Analyzing Naming Trends
boys = top1000[top1000.sex == 'M']
girls = top1000[top1000.sex == 'F']

total_births = pd.pivot_table(top1000, index='year', columns='name', values='births', aggfunc=np.sum)
print total_births

subset = total_births[['John', 'Harry', 'Mary', 'Marilyn']]
subset.plot(subplots=True, figsize=(12, 10), grid=False, title="Number of births per year")

# Measuring the increase in naming diversity
table = pd.pivot_table(top1000, index='year', columns='sex', values='prop', aggfunc=sum)
table.plot(title='Sum of table1000.prop by year and sex', yticks=np.linspace(0, 1.2, 13), xticks=range(1880, 2020, 10))

df = boys[boys.year == 2010]
print df[:10]

prop_cumsum = df.sort_values(by='prop', ascending=False).prop.cumsum()
print prop_cumsum[:10]
print prop_cumsum.searchsorted(0.5)

# 1990
df = boys[boys.year == 1900]
in1900 = df.sort_values(by='prop', ascending=False).prop.cumsum()
print in1900.searchsorted(0.5) + 1


def get_quantile_count(group, q=0.5):
    group = group.sort_values(by='prop', ascending=False)
    return group.prop.cumsum().searchsorted(q) + 1


diversity = top1000.groupby(['year', 'sex']).apply(get_quantile_count)
diversity = diversity.unstack('sex')
print diversity.head()
# diversity.plot(title="Number of popular names in top 50%")

# The “Last letter” Revolution
# extract last letter from name column
get_last_letter = lambda x: x[-1]
last_letters = names.name.map(get_last_letter)
last_letters.name = 'last_letter'
table = pd.pivot_table(names, index=last_letters, columns=['sex', 'year'], values='births', aggfunc=sum)
print table[:10]
subtable = table.reindex(columns=[1910, 1960, 2010], level='year')
print subtable.head()
print subtable.sum()
letter_prop = subtable / subtable.sum().astype(float)

# plot
fig, axes = plt.subplots(2, 1, figsize=(10, 8))
letter_prop['M'].plot(kind='bar', rot=0, ax=axes[0], title='Male')
letter_prop['F'].plot(kind='bar', rot=0, ax=axes[1], title='Female', legend=False)

letter_prop = table / table.sum().astype(float)
dny_ts = letter_prop.ix[['d', 'n', 'y'], 'M'].T
print dny_ts.head()
dny_ts.plot()

# Boy names that became girl names (and vice versa)
all_names = top1000.name.unique()
mask = np.array(['lesl' in x.lower() for x in all_names])
lesley_like = all_names[mask]
print lesley_like
filtered = top1000[top1000.name.isin(lesley_like)]
print filtered.groupby('name').births.sum()
table = pd.pivot_table(filtered, index='year', values='births', columns='sex', aggfunc=sum)
table = table.div(table.sum(1), axis=0)
print table.tail()
table.plot(style={'M': 'k-', 'F': 'k--'})
plt.show()