import re
from recommender import recommend_random, recommend_with_NMF, recommend_with_user_similarity
from flask import Flask,render_template,request
from utils import movies, methods_recommendation, get_movie_frame, create_user_vector

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
        movie=movies['title'].unique().tolist(),
        recommended_method = methods_recommendation,
        )
    # 'movies' variable is passed from python file to the html file for accessing it inside the html file

@app.route('/recommend')
def recommend():
    #read user input from url/webpage
    print(request.args)
    titles = request.args.getlist('title') # taking lists of titles only from user input
    ratings = request.args.getlist('rating') # taking lists of ratings only from user input
    methods = request.args.getlist('methode') # take the method to use
    print(titles,ratings,methods)
    #converting lists of titles and ratings into dict to pass to our recommender model
    user_rating = dict(zip(titles,ratings)) 
    if methods[0] == 'random':
        # movies is the imported DataFrame from the welcome() and user_rating is the user input
        movie_ids = recommend_random(movies, user_rating)
    elif methods[0] == 'NMF':
        movies_nmf = get_movie_frame(method = methods[0])
        new_user = create_user_vector(user_rating,movies_nmf)
        movie_ids = recommend_with_NMF(movies_nmf, new_user)
    elif methods[0] == 'user_similarity':
        movies_cs= get_movie_frame(method = methods[0])
        new_user = create_user_vector(user_rating,movies_cs)
        movie_ids = recommend_with_user_similarity(new_user, movies_cs)
    # renders the html page as the output of this function
    return  render_template('recommender.html',movie_ids=movie_ids) 
    # 'movie_ids' variable is passed from python file to the html file for accessing it inside the html file

# Runs the app (main module)
if __name__=='__main__':
    app.run(debug=True,port=5000)




