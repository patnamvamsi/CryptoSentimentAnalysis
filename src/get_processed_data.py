import pandas as pd

def get_processed_sentiment(twitter_handle):
    """
    Function to get the processed sentiment from the file.
    """
    processed_sentiment = pd.read_csv('../data/output/' + twitter_handle + '.csv')
    #processed_sentiment['timeline'] = processed_sentiment['timeline'].astype('Int64')
    return processed_sentiment


