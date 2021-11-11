import praw
from src.config import config
from src import BERT_Model as bert

equity_subreddits = 'wallstreetbets'
crypto_subreddits = 'SatoshiStreetBets'

reddit = praw.Reddit(client_id=config.REDDIT_CLIENT_ID,
                     client_secret=config.REDDIT_SECRET,
                     username=config.REDDIT_USERID,
                     password=config.REDDIT_PASWWORD,
                     user_agent=config.APP_NAME)

equity_subreddit = reddit.subreddit(equity_subreddits)
crypto_subreddit = reddit.subreddit(crypto_subreddits)

hot_equity = equity_subreddit.hot(limit=10)
hot_crypto = crypto_subreddit.hot(limit=10)

'''
Use recursion to retrive nested replies

'''

'''
for submission in hot_crypto:

    if not submission.stickied:
        print (submission)
        print(submission.title)
        print(submission.comments._comments[0].body)
        print (submission.comments._comments[0].reply)

        print(submission.comments._comments[1].body)
        print (submission.comments._comments[1].replies._comments[0].body)
        print (submission.comments._comments[1].replies._comments[0].replies._comments[0])
        print(submission.score) # upvotes-downvotes

'''

for comments in crypto_subreddit.stream.comments():
    print("Submission: Title: " + comments.link_title)
    print("Submission: Title: " + bert.get_sentiment(comments.link_title) )
    print("Score: " + str(comments.score))
    print("Comment: " + comments.body)
    print("Comment: " + bert.get_sentiment(comments.body))

'''Reddit Config
https://www.youtube.com/watch?v=qCB8MZ-W1Ig&ab_channel=EatTheBlocks
for equity: https://github.com/jklepatch/eattheblocks/blob/master/screencast/290-wallstreetbets-sentiment-analysis/reddit-sentiment-analysis.py
for crypro: https://github.com/jklepatch/eattheblocks/blob/master/screencast/294-cryptocurrency-sentiment-analysis/reddit-sentiment-analysis.py

subs = ['wallstreetbets', 'SatoshiStreetBets']
post_flairs = {'Daily Discussion','Weekend Discussion','Discussion'} # find more like news etc
goodUser = {'AutoModerator'} # users who can comment more than once
uniqueComment = True
upvoteRatio = 0.7
minCommentUpvotes = 2
minReplyUpvotes = 20
picks = 10 # define no of picks here , prints as "Top ## picks are:"
picks_ayz = 5 #define number of picks for sentiment analysis
'''

