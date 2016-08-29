# coding=utf-8
'''
@Title:movielens data processing

@Author: tyee.noprom@qq.com
@Time: 8/29/16 5:37 AM
'''

import pandas as pd
import numpy as np

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

# To get mean movie ratings for each film grouped by gender, we can use the pivot_table method
mean_ratings = pd.pivot_table(data, index='title', columns='gender', values='rating', aggfunc=np.mean)
print mean_ratings[:5]

ratings_by_title = data.groupby('title').size()
print ratings_by_title[:10]

# top 250 ratings
active_titles = ratings_by_title.index[ratings_by_title >= 250]
print active_titles

# top films among female viewers
top_female_ratings = mean_ratings.sort_values(by='F', ascending=False)
print top_female_ratings[:10]

# Measuring rating disagreement
mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
sorted_by_diff = mean_ratings.sort_values(by='diff')
print sorted_by_diff[:15]

# Reverse order of rows, take first 15 rows
print sorted_by_diff[:-1][:15]

# Standard deviation of rating grouped by title
rating_std_by_title = data.groupby('title')['rating'].std()
# Filter down to active_titles
rating_std_by_title = rating_std_by_title.ix[active_titles]
# Order Series by value in descending order
print rating_std_by_title.sort_values(ascending=False)[:10]