'''
1. EXTRACT the tweets from mongodb
-connect to a database
-query the data
2. TRANSFORM the data
-clean the text before?
-sentiment analysis
3. LOAD the data into postgres
-connect to postgres
-insert into postgress
'''
# 
import pymongo
import time
from sqlalchemy import create_engine
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import logging
import re
import pandas as pd


time.sleep(10)  # seconds

# Transform your tweets and create a dictionary
# Establish a connection with Postgres

USERNAME_PG = 'postgres'
PASSWORD_PG = 'postgres'
HOST_PG = 'postgres' # if in docker it would be the container name
PORT_PG = '5432'
DATABASE_NAME_PG = 'dbtweet'


### create connections to databases (check your mongosb and postgres in python notebooks (or luftdaten))
# Establish a connection to the MongoDB server
mongo_client = pymongo.MongoClient("mongodb", port=27017)
db = mongo_client.twitter
collection = db.twitter.find()

logging.critical(f"\n---- STEP OF DEBUGGING !!!!!!!11111111111!!!!!?????????????????? ----\n")
for tweet in collection:
    print(tweet['text'])


# Create the function that calculates polarity_scores and returns compund score

def polarity_score(text):
    analyzer  = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)['compound']
    return score

# Clean your tweets
mentions_regex= '@[A-Za-z0-9]+'
url_regex='https?:\/\/\S+' #this will not catch all possible URLs     ###add this to etl script
hashtag_regex= '#'
rt_regex= 'RT\s'

def clean_tweets(tweet):
    tweet = re.sub(mentions_regex, '', tweet)  #removes @mentions
    tweet = re.sub(hashtag_regex, '', tweet) #removes hashtag symbol
    tweet = re.sub(rt_regex, '', tweet) #removes RT to announce retweet
    tweet = re.sub(url_regex, '', tweet) #removes most URLs
    tweet=str(tweet)
    return tweet


# Connection string
conn_string_pg = f"postgresql://{USERNAME_PG}:{PASSWORD_PG}@{HOST_PG}:{PORT_PG}/{DATABASE_NAME_PG}" 
pg = create_engine(conn_string_pg,echo=False)
query1 = "CREATE table IF NOT EXISTS tweets (text VARCHAR(500), sentiment NUMERIC);"
pg.execute(query1)

logging.critical(f"\n---- AFTER CREATING TABLES WHAT!!!!!!?????????????????? ----\n")

# Transform your tweets and create a dictionary
cleantweets=[]
for tweet in collection:
    x = tweet['text']
    y= clean_tweets(x)
    cleantweets.append(y)


scores=[]
for tweet in cleantweets:
    scores.append(polarity_score(tweet))

# print(scores)

query2 = "INSERT INTO tweets VALUES (%s, %s);"
for text, score in zip(cleantweets, scores):#
    pg.execute(query1, (text, score))

# Explore the idea of live tweets collection withthe function 

#while works = True:
#   if tweet ...




# if you run everything through a function then enable this

#if __name__ == '__main__':  # this is for defining things



