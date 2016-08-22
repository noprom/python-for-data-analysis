# coding=utf-8
'''
@Title:usa.gov data clean

@Author: tyee.noprom@qq.com
@Time: 8/22/16 6:35 AM
'''

import json
from collections import defaultdict
from collections import Counter
from pandas import DataFrame, Series
import pandas as pd
import numpy as np

path = '../data/ch02/usagov_bitly_data2012-03-16-1331923249.txt'
print open(path).readline()
records = [json.loads(line) for line in open(path)]
print records[0]

# 获取列
print records[0]['tz']

# Counting Time Zones in Pure Python
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
print time_zones[:10]


def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in records:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts


def get_counts2(sequence):
    counts = defaultdict(int)  # values will initialize to 0
    for x in sequence:
        counts[x] += 1
    return counts


def top_counts(count_dict, n=10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]


counts = get_counts2(time_zones)
print counts['America/New_York']
print len(time_zones)
print top_counts(counts)

# 使用自带的类库
counts = Counter(time_zones)
print counts.most_common(10)

# Counting Time Zones with pandas
frame = DataFrame(records)
print frame
print frame['tz'][:10]
tz_counts = frame['tz'].value_counts()
print tz_counts[:10]

# filter na
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()
print tz_counts[:10]
# plot
tz_counts[:10].plot(kind='barh', rot=0)

results = Series([x.split()[0] for x in frame.a.dropna()])
print results[:5]
print results.value_counts()[:8]

cframe = frame[frame.a.notnull()]
print cframe
operating_system = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')
print operating_system[:5]
# group by
by_tz_os = cframe.groupby(['tz', operating_system])
agg_counts = by_tz_os.size().unstack().fillna(0)
print agg_counts[:10]

# Use to sort in ascending order
indexer = agg_counts.sum(1).argsort()
print indexer[:10]
count_subset = agg_counts.take(indexer)[-10:]
print count_subset
# plot
count_subset.plot(kind='barh', stacked=True)
normed_subset = count_subset.div(count_subset.sum(1), axis=0)
normed_subset.plot(kind='barh', stacked=True)
