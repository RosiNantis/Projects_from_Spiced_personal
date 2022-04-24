import tweepy
import pymongo
import twitter_keys
import logging


mongo_client = pymongo.MongoClient("mongodb")
db = mongo_client.twitter
collection = db.tweets

def tweet_what(max_res=100,save_tweet = False):
    """
    import tweepy and have the twitter key available at the same directory
    Gives what is tweeted on the subject you ask it. 
    tweet_what(*,max_res=100,save_tweet = False)
    -saves the weet in a specified folder
    -give the number of tweets you want to see
    """
    Bearer_Token = twitter_keys.Bearer_Token
    client = tweepy.Client(bearer_token=Bearer_Token)
    tok = 'bitcoin'
    search_query = ''.join(["#",tok, " -is:retweet"])
    #option to extract tweets of a particular language add `lang` parameter eg lang:de
    cursor = tweepy.Paginator(
        method=client.search_recent_tweets,
        query=search_query,
        tweet_fields=['id', 'created_at', 'text','lang','geo'],
        user_fields=['username']
    ).flatten(limit=max_res)
    #second_cursor = [tweet for tweet in cursor] # create a list with the items of cursor
    # cursor when it is operated in any way (e.g. print, save etc.. ) then it zeros. 
    for tweet in cursor:
        logging.critical(f'\n\n\nINCOMING TWEET:\n{tweet.text}\n\n\n')
         # create a json record and inserting it in the collections called tweets 
        record = {'text': tweet.text, 'id': tweet.id, 'created_at': tweet.created_at,'lang':tweet.lang,'geo':tweet.geo}
        # and inserting it in the collections called tweets 
        logging.critical(f"\n---- INSERTING A NEW tweet DOCUMENT INTO THE 'tweets' ----\n")
        db.tweets.insert_one(document=record)


    if save_tweet == True:
        file = open(tok+'.txt',mode='a',encoding='utf8')
        i = 1
        for tweet in cursor:
            file.write(str(i)+'. '+tweet.text+'\n\n\n\n')
            i = 1 + int(i)
        file.close()


if __name__ == '__main__':  # this is for defining things
    tweet_what(max_res=10,save_tweet = False)

