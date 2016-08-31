# coding=utf-8
'''
@Title: Basic Profiling: %prun and %run -p
        Usage: python -m cProfile cprofile.py
               python -m cProfile -s cumulative cprofile.py
@Author: tyee.noprom@qq.com
@Time: 8/31/16 8:17 AM
'''
import numpy as np
from numpy.linalg import eigvals

def run_experiment(niter=100):
    K = 100
    results = []
    for _ in xrange(niter):
        mat = np.random.randn(K, K)
        max_eigenvalue = np.abs(eigvals(mat)).max()
        results.append(max_eigenvalue)
        return results


some_results = run_experiment()
print 'Largest one we saw: %s' % np.max(some_results)

