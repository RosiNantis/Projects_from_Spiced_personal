import pymongo
import time
from sqlalchemy import create_engine
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

time.sleep(10)  # seconds

# Establish a connection to the MongoDB server
client = pymongo.MongoClient(host="mongodb", port=27017)

# Select the database you want to use withing the MongoDB server
db = client.twitter
collection = db.tweets



#connection to postgres

engine = create_engine('postgresql://postgres:postgres@postgres:5432/tweets', echo=True)

# create a table
engine.execute('''
    CREATE TABLE IF NOT EXISTS tweets (
    text VARCHAR(500),
    sentiment NUMERIC
);
''')

# creating a vader sentiment analyzer
s = SentimentIntensityAnalyzer()

docs = db.tweets.find()
for tweet in docs:
    tweet_text = tweet['text']
    sentiment = s.polarity_scores(tweet_text)  # assuming your JSON docs have a text field
    score = sentiment['compound']
    query = "INSERT INTO tweets VALUES (%s, %s);"
    engine.execute(query, (tweet_text, score))
    print(sentiment)