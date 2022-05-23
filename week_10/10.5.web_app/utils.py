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
umrT = pd.read_csv('../data/ml-latest-small/ratings.csv', na_values = 'Nan')
mtg = pd.read_csv('../data/ml-latest-small/movies.csv', na_values = 'Nan')
# merge the two frames based on the column movieid
movies = pd.merge(umrT, mtg, on='movieId')

methods_recommendation = ['random','NMF','user_similarity']

# load model
with open('static/model5.pkl', 'rb') as f:
    model= pickle.load(f)


def get_movie_frame(method = methods_recommendation, umrT=umrT, mtg = mtg):

    if method == 'NMF':
        """
        i will get a Data Frame with movieId Title and userId 
        pivoted in a matrix with NaN where user has no rating
        """
        # use pivot to make the matrix of movie rates
        rates =umrT.pivot(index='userId',columns = 'movieId')
        # Split the movie name from movie year and apply it in the matrix
        mtg['year'] = mtg.title.astype(str).str[-6:]
        mtg['title_new'] = mtg.title.astype(str).str[:-6]
        # Try to zip columns with movie names
        #new_columns = dict(zip(df.movieId,df_movie.title))
        rates.rename(columns=dict(zip(mtg["movieId"], mtg["title_new"])),inplace = True)
        movies = rates.rating
    elif method == 'user_similarity':
        """
        i will get a Data Frame with movieId Title average ratings for per user.
        Final outcome is a frame with columns:# 
        movieID, userID, avg(rate), title, genres, accurate(rate)
        """
        umrT_av_rat = umrT.set_index('movieId').groupby(['movieId']).mean()
        # merge the two frames based on the column movieid
        movies = pd.merge(umrT, mtg, on='movieId')
        # merge the two frames based on the column movieid to find average rating
        movieId_rating = pd.merge(umrT_av_rat, mtg, on='movieId')
        # merge movieID, userID, avg(rate), title, genres, accurate(rate)
        mov = pd.merge(movieId_rating,movies, on='movieId', how = 'left')[["movieId", "rating_x","title_x","userId_y","genres_x","rating_y"]]
        mov.columns = [["movieId", "rating_avg","title","userId","genres","rating_acc"]]
        # reset index
        movies = mov
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

