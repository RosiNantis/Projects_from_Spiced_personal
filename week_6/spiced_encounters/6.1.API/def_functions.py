def route(duration = 10):

    """
    The function gives all the possible trains/busses etc. It requests for the station
    and if needed as an arguement the length of duration. It responds with the delay 
    along with the different roots.
    """
    import requests
    departure = input('\nWhich station is the departure point:\n')
    url = f"https://v5.vbb.transport.rest/locations?poi=false&addresses=false&query={departure}"
    station_id = requests.get(url).json()[0]['id']
    print(f'\nNext connections from {departure}:\n')
    url = f'https://v5.vbb.transport.rest/stops/{station_id}/departures?duration={duration}'
    my_url_list = requests.get(url).json()
    for choises in my_url_list:
        print(choises['plannedWhen'][11:-9], '  ', choises['line']['name'], choises['direction'],'. There are',round(choises['delay']/60,0),' min delay.')
 


def tweet_who(max_res=100,save_tweet = False):
    """
    import tweepy and have the twitter key available at the same directory
    Gives what is tweeted of the person said. 
    tweet_who(*,max_res=100,save_tweet = False)
    -saves the weet in a specified folder
    -give the number of tweets you want to see
    """
    import tweepy
    import twitter_keys
    client = tweepy.Client(bearer_token=twitter_keys.Bearer_Token)
    give_username = input('\nWhich user should I look for:\n')
    user = client.get_user(username=give_username,user_fields=['name','id','created_at'])
    what = user.data
    user_tweets = client.get_users_tweets(id=what.id, tweet_fields=['id','text','created_at'],max_results=max_res)
    for tweet in user_tweets.data:
        print(f"The user {give_username} wrote: '{tweet.text}'\n")
    if save_tweet == True:
        for tweet in user_tweets.data:
            file = open('tweets/',give_username,'.txt',mode='a',encoding='utf8')
            file.write('\n\n'+tweet.text)
            file.close()



def tweet_what(max_res=100,save_tweet = False):
    """
    import tweepy and have the twitter key available at the same directory
    Gives what is tweeted on the subject you ask it. 
    tweet_what(*,max_res=100,save_tweet = False)
    -saves the weet in a specified folder
    -give the number of tweets you want to see
    """
    import tweepy
    import twitter_keys
    client = tweepy.Client(bearer_token=twitter_keys.Bearer_Token)
    tok = input('\nWhat should I search:\n')
    search_query = ''.join(["#",tok, " -is:retweet"])
    #option to extract tweets of a particular language add `lang` parameter eg lang:de
    cursor = tweepy.Paginator(
        method=client.search_recent_tweets,
        query=search_query,
        tweet_fields=['author_id', 'created_at', 'public_metrics'],
        user_fields=['username']
    ).flatten(limit=max_res)
    for tweet in cursor:
        print(f"The user {tweet.id} tweeted on {tweet.created_at} : '{tweet.text}'\n")
    if save_tweet == True:
        for tweet in cursor:
            file = open('tweets/',tok,'.txt',mode='a',encoding='utf8')
            file.write('\n\n'+tweet.text)
            file.close()



# if __name__ == '__main__':  # this is for defining things
#     route(number_of_list=10)