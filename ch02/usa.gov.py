# coding=utf-8
'''
@Title:usa.gov data clean

@Author: tyee.noprom@qq.com
@Time: 8/22/16 6:35 AM
'''

import json

path = '../data/ch02/usagov_bitly_data2012-03-16-1331923249.txt'
print open(path).readline()
records = [json.loads(line) for line in open(path)]
print records[0]