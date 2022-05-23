"""
UTILS 
- Helper functions to use for your recommender funcions, etc
- Data: import files/models here e.g.
    - movies: list of movie titles and assigned cluster
    - ratings
    - user_item_matrix
    - item-item matrix 
- Models:
    - nmf_model: trained sklearn NMF model
"""
import pandas as pd
import numpy as np
from fuzzywuzzy import process
import pickle


#movies = pd.read_csv('movies_ratings.csv', index_col=0)
umrT = pd.read_csv('../data/ml-latest-small/ratings.csv', na_values = 'Nan',index_col=0)
mtg = pd.read_csv('../data/ml-latest-small/movies.csv', na_values = 'Nan',index_col=0)
# merge the two frames based on the column movieid
movies = pd.merge(umrT, mtg, on='movieId')




methods_recommendation = ['random','NMF','user_similarity']

# load model
with open('static/model5.pkl', 'rb') as f:
    model= pickle.load(f)

def get_movie_frame(umrT=umrT, mtg = mtg):
    """
    i will get a Data Frame with movieId Title average ratings for per user
    """
    umrT_av_rat = umrT.set_index('movieId').groupby(['movieId']).mean()
    # merge the two frames based on the column movieid
    movies = pd.merge(umrT_av_rat, mtg, on='movieId')
    # reset index
    movies = movies.reset_index()
    return movies

def match_movie_title(input_title, movie_titles):
    """
    Matches inputed movie title to existing one in the list with fuzzywuzzy
    """
    matched_title = process.extractOne(input_title, movie_titles)[0]

    return matched_title

def print_movie_titles(movie_titles):
    """
    Prints list of movie titles in cli app
    """    
    for movie_id in movie_titles:
        print(f'            > {movie_id}')

def create_user_vector(user_rating, movies):
    """
    Convert dict of user_ratings to a user_vector
    """       
    # generate the user vector
    print(user_rating)
    user_vector = None
    return user_vector


def lookup_movieId(movies, movieId):
    """
    Convert output of recommendation to movie title
    """
    # match movieId to title
    movies = movies.reset_index()
    boolean = movies["movieId"] == movieId
    movie_title = list(movies[boolean]["title"])[0]
    return movie_title

