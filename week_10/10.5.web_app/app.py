import re
from recommender import recommend_random, recommend_with_NMF, recommend_with_user_similarity
from flask import Flask,render_template,request
from utils import movies, methods_recommendation

# # example input of web application
# user_rating = {
#     'the lion king': 5,
#     'terminator': 5,
#     'star wars': 2
# }



# construct our flask instance, pass name of module
app = Flask(__name__)


# route decorator for mapping urls to functions
@app.route('/')
def welcome():
    # renders the html page as the output of this function
    return render_template(
        'index.html',
        name="Stationary Srirachas 🌶",
        movies=movies['title'].tolist(),
        recommended_method = methods_recommendation,
        )
    # 'movies' variable is passed from python file to the html file for accessing it inside the html file

@app.route('/recommend')
def recommend():
    #read user input from url/webpage
    print(f'I recommend!!!!!{request.args}')
    titles = request.args.getlist('title') # taking lists of titles only from user input
    ratings = request.args.getlist('rating') # taking lists of ratings only from user input
    methods = request.args.getlist('methods')
    print(f'The method used for the recommendation is {methods}')
    # print(titles,ratings,methods)
    # # converting lists of titles and ratings into dict to pass to our recommender model
    # user_rating = dict(zip(titles,ratings)) 
    # if methods == 'random':
    #     movie_ids = recommend_random(movies, user_rating)
    # elif methods == 'NMF':
    #     movie_ids = recommend_with_NMF
    # else:
    #     movie_ids = recommend_with_user_similarity
    # # renders the html page as the output of this function
    # return  render_template('recommender.html',movie_ids=movie_ids) 
    # # 'movie_ids' variable is passed from python file to the html file for accessing it inside the html file


# Runs the app (main module)
if __name__=='__main__':
    app.run(debug=True,port=5000)




