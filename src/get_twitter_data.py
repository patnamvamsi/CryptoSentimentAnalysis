import json
import tweepy
from src.config import config
import pandas as pd


consumer_key = config.TWITTER_API_KEY
consumer_secret = config.TWITTER_SECRET_KEY
access_token = config.TWITTER_ACCESS_TOKEN
access_token_secret = config.TWITTER_TOKEN_SECRET

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

def get_user_tweets(username, count):

    try:

        tweets = tweepy.Cursor(api.user_timeline,tweet_mode='extended', id=username).items(count)
        tweets_list = [[tweet.created_at, tweet.id, tweet.text] for tweet in tweets]
        tweets_df = pd.DataFrame(tweets_list)
        print(tweets_df.to_csv())
    except BaseException as e:
        print('failed on_status,', str(e))

def get_all_user_tweets(userid):

    tweets = []
    for tweet in tweepy.Cursor(api.user_timeline,tweet_mode='extended', id=userid).items():
        tweets.append(tweet._json)
        print(tweet._json)

    with open(config.input_data + userid + '.json', 'w') as f:
        json.dump(tweets, f)

    return tweets.__len__()

def get_text_search_tweets(query,count):

    #text_query = '2020 US Election'
    #count = 150
    try:
        tweets = tweepy.Cursor(api.search,tweet_mode='extended', q=query).items(count)
        tweets_list = [[tweet.created_at, tweet.id, tweet.text] for tweet in tweets]
        tweets_df = pd.DataFrame(tweets_list)
        print(tweets_df.to_csv())
    except BaseException as e:
        print('failed on_status,', str(e))

    return tweets_df[2]

def test_case():
    #_get_all_user_tweets('intocryptoverse')
    tweet_count = get_all_user_tweets('ThinkingCrypto1')
    #_get_all_user_tweets('aantonop')
    '''
    tweets = get_user_tweets('intocryptoverse', 10)
    #tweets = get_text_search_tweets('xrp', 10)
    
    for tweet in tweets:
        print (tweet)
        #print (bert.get_sentiment(tweet))
    '''
    return tweet_count
if __name__ == "__main__":
    #test_case()
    print ("Main called")

''''
open issues: 
ex tweet:
RT @AlexCobb_: Once XRP is done with this consolidation it’s gonna go for a HUGE rip
Bears are pathetic on the weekly chart, bulls will en…

the first sentence is a +ve note for xrp, but the following one is negative yet unrelated.
the output has come out as neutral from BERT.

need to divide and calculate tweets seperatley and then consolidate together later.

https://twitter.com/intocryptoverse
https://twitter.com/ThinkingCrypto1
https://twitter.com/aantonop

analysing  in pandas
https://www.kdnuggets.com/2017/03/beginners-guide-tweet-analytics-pandas.html

'''
