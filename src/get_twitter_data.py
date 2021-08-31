import tweepy
from config import config
import pandas as pd
from src import BERT_Model as bert

consumer_key = config.TWITTER_API_KEY
consumer_secret = config.TWITTER_SECRET_KEY
access_token = config.TWITTER_ACCESS_TOKEN
access_token_secret = config.TWITTER_TOKEN_SECRET

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

def get_user_tweets(username, count):

    try:

        tweets = tweepy.Cursor(api.user_timeline, id=username).items(count)
        tweets_list = [[tweet.created_at, tweet.id, tweet.text] for tweet in tweets]
        tweets_df = pd.DataFrame(tweets_list)
        print(tweets_df.to_csv())
    except BaseException as e:
        print('failed on_status,', str(e))


def get_text_search_tweets(query,count):

    #text_query = '2020 US Election'
    #count = 150
    try:
        tweets = tweepy.Cursor(api.search, q=query).items(count)
        tweets_list = [[tweet.created_at, tweet.id, tweet.text] for tweet in tweets]
        tweets_df = pd.DataFrame(tweets_list)
        print(tweets_df.to_csv())
        #print ([tweet] for tweet in tweets)
    except BaseException as e:
        print('failed on_status,', str(e))

    return tweets_df[2]

def test_case():
    get_user_tweets('jack', 10)
    tweets = get_text_search_tweets('xrp', 10)
    for tweet in tweets:
        print (tweet)
        print (bert.get_sentiment(tweet))



if __name__ == "__main__":
    test_case()

''''
open issues: 
ex tweet:
RT @AlexCobb_: Once XRP is done with this consolidation it’s gonna go for a HUGE rip
Bears are pathetic on the weekly chart, bulls will en…

the first sentence is a +ve note for xrp, but the following one is negative yet unrelated.
the output has come out as neutral from BERT.

need to divide and calculate tweets seperatley and then consolidate together later.
'''
