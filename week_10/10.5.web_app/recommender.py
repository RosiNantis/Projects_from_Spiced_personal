"""
Contains various recommondation implementations
all algorithms return a list of movieids
"""

import pandas as pd
import numpy as np
from utils import lookup_movieId, match_movie_title, model, create_user_vector


def recommend_random(movies, user_rating, k=5):
    """
    return k random unseen movies for user 
    """
    # makes a frame for the external user ratings of the movies(features)
    user = pd.DataFrame(user_rating, index=[0])
    # rearrange the frame as movies and ratings two columns, movies and ratings
    user_t = user.T.reset_index()
    # list of the entry movies
    user_movie_entries = list(user_t["index"])
    # list of the movie titles of library
    movie_titles = list(movies["title"])
    # matches the movies from user with the library
    intended_movies = [match_movie_title(title, movie_titles) for title in user_movie_entries]
    
    # convert these movies to intended movies and convert them into movie ids
    recommend = movies.copy()
    recommend = recommend.reset_index()
    recommend = recommend.set_index("title")
    recommend.drop(intended_movies, inplace=True)
    random_movies = np.random.choice(list(recommend.index), replace=False, size=k)
    return random_movies  



#def recommend_with_NMF(user_item_matrix, user_rating, model, k=5):
def recommend_with_NMF(movies, user_rating, k = 5):
    """
    NMF Recommender
    INPUT
    - user_vector with shape (1, #number of movies)
    - user_item_matrix
    - trained NMF model
    OUTPUT
    - a list of movieIds
    """
    
    # initialization - impute missing values    
    new_user = create_user_vector(user_rating)
    movies_all_users = pd.concat([new_user, movies], axis = 0,ignore_index=True) 
    # transform user vector into hidden feature space
    
    # inverse transformation

    # build a dataframe

    # discard seen movies and sort the prediction
    
    # return random_movies  
    #return 'it works'

def recommend_with_user_similarity(user_item_matrix, user_rating, k=5):
    # initiate a new user




    # return random_movies  
    pass


