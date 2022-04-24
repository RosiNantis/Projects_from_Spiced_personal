'''
1. 
2. 
3. 
'''
# 
import pymongo 
from sqlalchemy import create_engine
import logging
import re
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


### create connections to databases (check your mongosb and postgres in python notebooks (or luftdaten))
# Establish a connection to the MongoDB server
import time

time.sleep(10)

client = pymongo.MongoClient(host="mongo_db", port=27017)

# Select the database you want to use withing the MongoDB server
db = client.collect_tweets
tweets=db.collect_tweets.find()


#Add postgres credentials
DATABASE = 'postgres_db_twitter'
PORT = '5432'
USER = "postgres"
PASSWORD = "postgres"
HOST = 'postgresdb'

# Establish a connection with Postgres
conn_string = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'
query= " CREATE TABLE IF NOT EXISTS tweets (text VARCHAR(500), sentiment NUMERIC);"
engine = create_engine(conn_string,echo=False)
engine.execute(query)

# Create the function that calculates polarity_scores and returns compund score
def polarity_score(tweet):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(tweet)['compound']
    return score


# Function that cleans tweets

mentions_regex= '@[A-Za-z0-9]+'
url_regex='https?:\/\/\S+' #this will not catch all possible URLs
hashtag_regex= '#'
rt_regex= 'RT\s'

def clean_tweets(tweet):
    tweet = re.sub(mentions_regex, '', tweet)  #removes @mentions
    tweet = re.sub(hashtag_regex, '', tweet) #removes hashtag symbol
    tweet = re.sub(rt_regex, '', tweet) #removes RT to announce retweet
    tweet = re.sub(url_regex, '', tweet) #removes most URLs
    tweet=str(tweet)
    print(type(tweet))
    return tweet

# Transform your tweets and create a dictionary
cleantweets=[]
for tweet in tweets:
    x = tweet['text']
    # print('print XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',x)
    # print(type(x))
    y= clean_tweets(x)
    cleantweets.append(y)

scores=[]
for tweet in cleantweets:
    scores.append(polarity_score(cleantweets))

print(scores)

query1 = "INSERT INTO tweets VALUES (%s, %s);"
for text, score in zip(cleantweets, scores):#
    engine.execute(query1, (text, score))

# df = pd.DataFrame({'text':cleantweets,'sentiment':score})

# #Load your tweets into a postgres database
# df.to_sql('tweets',engine,if_exists='replace') 