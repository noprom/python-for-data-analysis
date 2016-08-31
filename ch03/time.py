# coding=utf-8
'''
@Title:Timing Code: %time and %timeit

@Author: tyee.noprom@qq.com
@Time: 8/31/16 8:05 AM
'''

# Timing Code: %time and %timeit

# a very large list of strings
strings = ['foo', 'foobar', 'baz', 'qux', 'python', 'Guido Van Rossum'] * 100000
method1 = [x for x in strings if x.startswith('foo')]
method2 = [x for x in strings if x[:3] == 'foo']


# %time method1 = [x for x in strings if x.startswith('foo')]
# %time method2 = [x for x in strings if x[:3] == 'foo']
# %timeit [x for x in strings if x.startswith('foo')]
# %timeit [x for x in strings if x[:3] == 'foo']
