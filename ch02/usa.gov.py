# coding=utf-8
'''
@Title:usa.gov data clean

@Author: tyee.noprom@qq.com
@Time: 8/22/16 6:35 AM
'''

import json
from collections import defaultdict

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
