import pymongo
import tweepy
import twitter_keys

# connect to mongodb container
client_docker = pymongo.MongoClient(host="mongo_db",port=27017)
db = client_docker.collect_tweets


client = tweepy.Client(bearer_token=twitter_keys.Bearer_Token)

query = "#electionpresidentielle -is:retweet -is:reply -is:quote -has:links"
search_tweets = client.search_recent_tweets(query=query,tweet_fields=['id','created_at','text'], max_results=100)
print(search_tweets)
print(type(search_tweets))

for tweet in search_tweets.data:
    record = {'text': tweet.text, 'id': tweet.id, 'created_at': tweet.created_at}
    db.collect_tweets.insert_one(document=record)
