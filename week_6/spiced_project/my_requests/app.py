import tweepy
import twitter_keys

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
    tok = input('\nWhat should I search:\n')
    search_query = ''.join(["#",tok, " -is:retweet"])
    #option to extract tweets of a particular language add `lang` parameter eg lang:de
    cursor = tweepy.Paginator(
        method=client.search_recent_tweets,
        query=search_query,
        tweet_fields=['author_id', 'created_at', 'public_metrics'],
        user_fields=['username']
    ).flatten(limit=max_res)
    second_cursor = [tweet for tweet in cursor] # create a list with the items of cursor
    # cursor when it is operated in any way (e.g. print, save etc.. ) then it zeros. 
    for tweet in second_cursor:
        print(f"The user {tweet.id} tweeted on {tweet.created_at} : '{tweet.text}'\n")
    if save_tweet == True:
        file = open(tok+'.txt',mode='a',encoding='utf8')
        i = 1
        for tweet in second_cursor:
            file.write(str(i)+'. '+tweet.text+'\n\n\n\n')
            i = 1 + int(i)
        file.close()


if __name__ == '__main__':  # this is for defining things
    tweet_what(max_res=100,save_tweet = True)