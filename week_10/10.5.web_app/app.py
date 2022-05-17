from recommender import recommend_random
from flask import Flask
from utils import movies, print_movie_titles
# example input of web application
user_rating = {
    'the lion king': 5,
    'terminator': 5,
    'star wars': 2
}

app = Flask(__name__) # to initialize the Flask application we put __name__ if nth else is to be included
def welcome():
    return 'Hello welcome to my app'


# Please make sure that you output the ids and then modify the lookupmovieId to give the user the titles

### Terminal recommender:

# print('>>>> Here are some movie recommendations for you<<<<')
# print('')
# print('Random movies')
# movie_ids = recommend_random(movies, user_rating)
# print(movie_ids)


