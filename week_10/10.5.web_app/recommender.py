"""
Contains various recommondation implementations
all algorithms return a list of movieids
"""

import pandas as pd
import numpy as np
from utils import  match_movie_title, model, create_user_vector, get_movie_frame, clean_nan_numbers
from sklearn.impute import SimpleImputer


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


    
def recommend_with_NMF(movies ,new_user, model=model, k=5):
    """
    NMF Recommender
    INPUT
    - user_vector with shape (1, #number of movies)
    - user_item_matrix
    - trained NMF model
    OUTPUT
    - a list of movieIds
    """
    table = pd.concat([new_user, movies], axis = 0,ignore_index=True) 
    # ------------------------------------------------------------#  
    #  dEal with missing values with Imputer
    packet= clean_nan_numbers(table)
    clean_table=packet[0]
    imputer = packet[1]

    # ------------------------------------------------------------#  
    # take Q and P matrices
    Q = model.components_
    P = model.transform(clean_table)
    # ------------------------------------------------------------#  
    # locate new user and give an array of rates with Imputed values
    user = table.iloc[0,:].values
    user = user.reshape(1, -1)
    # ------------------------------------------------------------#
    # predict user P, R values
    user_clean = imputer.transform(user)
    user_P = model.transform(user_clean) 
    user_R = np.dot(user_P,Q)
    # ------------------------------------------------------------#
    # remove seen movies & give top n recommendations   
    recommendation = pd.DataFrame({'user_input':user[0], 'predicted_ratings':user_R[0]}, index = table.columns)
    recommendation = recommendation[recommendation['user_input'].isna()].sort_values(by = 'predicted_ratings', ascending= False)
    NMF_movies = list(recommendation.iloc[:k].index)
    return NMF_movies



def recommend_with_user_similarity(user_item_matrix, user_rating, k=5):
    # initiate a new user




    # return random_movies  
    pass


