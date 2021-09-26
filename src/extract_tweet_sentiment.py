import datetime
import json
import glob
import pandas as pd
from collections import OrderedDict
from src.BERT_Model import get_financial_sentiment
import time

input_dir = 'C:\\Dev\\Projects\\CryptoSentimentAnalysis\\data\\input'
output_dir = 'C:\\Dev\\Projects\\CryptoSentimentAnalysis\\data\\output'
BATCH_SIZE = 500

def extract_sentiment(filename,output_dir):
    f = open(input_dir + '\\' + filename,)
    data = json.load(f,object_pairs_hook=OrderedDict)
    count = len(data)
    li = []
    tw_list = []
    for tweets in data:
        tw_list.append(tweets['full_text'])

    '''
    enhance to implement in batch
    print (time.perf_counter())
    get_financial_sentiment(tw_list)
    print(time.perf_counter())
    '''
    for tweets in data:
        time_line = datetime.datetime.strptime(tweets['created_at'], '%a %b %d %H:%M:%S %z %Y').timestamp()
        tweet = tweets['full_text']
        sentiment = get_financial_sentiment(tweets['full_text'])
        label = sentiment[0]['label']
        score = sentiment[0]['score']
        li.append([time_line,tweet,label,score])
        count = count = count -1
        print (count)
        print ([time_line,tweet,label,score])

    df = pd.DataFrame(li, columns=['timeline', 'tweet', 'label', 'score'])
    df.reset_index(drop=True, inplace=True)
    df.to_csv(output_dir + '\\' + filename.replace(".json", ".csv"), index=False)


def process_tweet_files(input_dir, output_dir):
    all_files = glob.glob(input_dir + '\\' + "/*")
    print(all_files)
    for filename in all_files:
        extract_sentiment(filename.split('\\')[-1],output_dir)


if __name__ == "__main__":
    input_dir  = 'C:\\Dev\\Projects\\CryptoSentimentAnalysis\\data\\input'
    output_dir = 'C:\\Dev\\Projects\\CryptoSentimentAnalysis\\data\\output'
    process_tweet_files(input_dir,output_dir)

