from flask import Flask
from simple_recommender import get_recommendations
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello_sriracha():
    return render_template(
    "main_external.html", title="Welcome Sriracha!"
    )


@app.route("/recommendations")
def recommender():

    top3=get_recommendations()

    return render_template(
    "recommendations.html",
    movies=top3)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
