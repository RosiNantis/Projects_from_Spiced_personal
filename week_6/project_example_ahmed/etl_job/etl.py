
import time
import logging
import pymongo
import random
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from sqlalchemy import create_engine

client = pymongo.MongoClient("mongodb://mongodb:27017/")
db = client.tweets

pg = create_engine('postgres://postgres@postgresdb:5432')
pg.execute('''CREATE TABLE IF NOT EXISTS tweets (
    text VARCHAR(512),
    sentiment NUMERIC
);
''')


def read_tweet_from_mongo():
    """gets a random tweet"""
    tweets = list(db.collections.data_science.find())
    if tweets:
        t = random.choice(tweets)
        logging.critical("random tweet: " + t['text'])
        return t

def calc_sentiment(tweet):
    s  = SentimentIntensityAnalyzer()
    sentiment = s.polarity_scores(tweet['text'])
    logging.critical("sentiment: " + str(sentiment))
    return sentiment['compound']


def write_tweet_to_postgres(tweet, sentiment):
    # GOOD BUT MAYBE NOT WORKING:
    #pg.execute(f"INSERT INTO tweets VALUES (?,?);", (tweet["text"], sentiment))
    # BAD BUT PROBABLY WORKS
    pg.execute(f"""INSERT INTO tweets VALUES ('{tweet["text"]}', {sentiment});""")
    logging.critical("tweet + sentiment written to pg")

# define an Airflow task
#read_tweet_from_mongo >> calc_sentiment >> write_tweet_to_postgres


logging.critical("Hello from the ETL job")
while True:
    tweet = read_tweet_from_mongo()
    if tweet:
        sent = calc_sentiment(tweet)
        write_tweet_to_postgres(tweet, sent)
    time.sleep(10)
