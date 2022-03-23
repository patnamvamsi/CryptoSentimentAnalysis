import json
from datetime import datetime

import sqlalchemy
import tweepy
from config import config
import pandas as pd
from db.timescaledb import connect_postgres as db


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


def get_all_user_tweets(userid, since):
    print(since)
    tweets = []
    for tweet in tweepy.Cursor(api.user_timeline, since_id=since, tweet_mode='extended', id=userid).items():

        tweets.append([datetime.strftime(datetime.strptime(tweet._json['created_at'], '%a %b %d %H:%M:%S +0000 %Y'),
                                         '%Y-%m-%d %H:%M:%S'),
                      userid, 'twitter', tweet._json])
        print(tweet._json)

    tweets_df = pd.DataFrame(tweets, columns=['timeline', 'handle', 'source', 'raw_message']) # ,'raw_message_text','status'

    conn = db.create_sqlalchemy_engine_conn()

    tweets_df.to_sql('raw_messages', conn, if_exists='append', index=False, dtype = {'raw_message': sqlalchemy.types.JSON} )

    """ Write to a file
    with open(config.input_data + userid + '.json', 'w') as f:
        json.dump(tweets, f)
    """

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


def get_last_updated_tweets():

    conn = db.create_sqlalchemy_engine_conn()
    query = 'select handle, max (raw_message ->> \'id\') since_id from raw_messages where source = \'twitter\' group by handle'
    last_updated_tweet = pd.read_sql(query, conn)
    print(last_updated_tweet)
    return last_updated_tweet

def update_db_with_latest_tweets():

    df = get_last_updated_tweets()
    for index, row in df.iterrows():
        get_all_user_tweets(row['handle'],  row['since_id'])
        print(row['handle'], row['since_id'] )


def test_case():

    print("Causes dupicates -- careful")
    #tweet_count = get_all_user_tweets('ThinkingCrypto1', 1)
    #print("tweets processed: " + str(tweet_count))

    #tweet_count = get_all_user_tweets('aantonop', 1)
    #print("tweets processed: " + str(tweet_count))

    #tweet_count = get_all_user_tweets('intocryptoverse', 1)
    #print("tweets processed: " + str(tweet_count))
    #return tweet_count


if __name__ == "__main__":
    #test_case()
    update_db_with_latest_tweets()

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
