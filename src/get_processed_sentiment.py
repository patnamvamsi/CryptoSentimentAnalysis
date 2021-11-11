import pandas as pd

def get_processed_sentiment(twitter_handle):
    """
    Function to get the processed sentiment from the file.
    """
    processed_sentiment = pd.read_csv('../data/output/' + twitter_handle + '.csv')
    return processed_sentiment


