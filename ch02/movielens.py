# coding=utf-8
'''
@Title:movielens data processing

@Author: tyee.noprom@qq.com
@Time: 8/29/16 5:37 AM
'''

import pandas as pd

movie_lens_data_path = '../data/ch02/movielens/'
unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table(movie_lens_data_path + 'users.dat', sep='::', header=None, names=unames, engine='python')

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table(movie_lens_data_path + 'ratings.dat', sep='::', header=None, names=rnames, engine='python')

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table(movie_lens_data_path + 'movies.dat', sep='::', header=None, names=mnames, engine='python')

print users[:5]
print ratings[:5]
print movies[:5]

# merge all the data
data = pd.merge(pd.merge(ratings, users), movies)
print data[:1]
print data.ix[0]