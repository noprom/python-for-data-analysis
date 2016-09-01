# coding=utf-8
'''
@Title: Random Number Generation

@Author: tyee.noprom@qq.com
@Time: 9/1/16 5:09 PM
'''

import numpy as np
import random
from random import normalvariate

samples = np.random.normal(size=(4, 4))
samples

N = 1000000
samples = [normalvariate(0, 1) for _ in xrange(N)]
np.random.normal(size=N)

# Example: Random Walks

position = 0
walk = [position]
steps = 1000
for i in xrange(steps):
    step = 1 if random.randint(0, 1) else -1
    position += step
    walk.append(position)

nsteps = 1000
draws = np.random.randint(0, 2, size=nsteps)
steps = np.where(draws > 0, 1, -1)
walk = steps.cumsum()
walk.min()
walk.max()
(np.abs(walk) >= 10).argmax()

# Simulating Many Random Walks at Once
nwalks = 5000
nsteps = 1000
draws = np.random.randint(0, 2, size=(nwalks, nsteps))  # 0 or 1
steps = np.where(draws > 0, 1, -1)
walks = steps.cumsum(1)
walks.max()
walks.min()

hits30 = (np.abs(walks) >= 30).any(1)
hits30.sum()  # Number that hit 30 or -30
crossing_times = (np.abs(walks[hits30]) >= 30).argmax(1)
crossing_times.mean()