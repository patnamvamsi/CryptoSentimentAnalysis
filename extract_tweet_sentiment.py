import datetime
import json
import glob
import pandas as pd
from collections import OrderedDict
from BERT_Model import get_financial_sentiment
from config import config
from db.timescaledb import connect_postgres as db


input_dir = config.input_data
output_dir = config.output_data
BATCH_SIZE = 100

def fetch_unprocessed_raw_messages():

    conn = db.create_sqlalchemy_engine_conn()
    query = 'select id,raw_message from raw_messages where source = \'twitter\' and status is null limit ' + str(BATCH_SIZE)
    raw_data = pd.read_sql(query, conn)
    return raw_data


def write_sentiment_to_db(df):

    conn = db.create_sqlalchemy_engine_conn()
    df.to_sql('mytemptable', conn, index=False, if_exists='replace')
    query = 'insert into processed_sentiments  select id,to_timestamp(timeline),source,message,label,score from mytemptable; ' \
            'update raw_messages set status = \'processed\' where id in (select id from mytemptable);'
    conn.execute(query)


def extract_sentiment():
    """
    f = open(input_dir + '/' + filename, )
    data = json.load(f, object_pairs_hook=OrderedDict)
    count = len(data)
    """
    li = []

    data = fetch_unprocessed_raw_messages()
    count = data.shape[0]

    '''
    tw_list = []
    for tweets in data:
        tw_list.append(tweets['full_text'])

    enhance to implement in batch
    print (time.perf_counter())
    get_financial_sentiment(tw_list)
    print(time.perf_counter())
    '''
    for x,row in data.iterrows():

        tweets = row['raw_message']
        id = row['id']
        time_line = datetime.datetime.strptime(tweets['created_at'], '%a %b %d %H:%M:%S %z %Y').timestamp()
        tweet = tweets['full_text'].replace("\n", "").replace("\r", "")
        sentiment = get_financial_sentiment(tweet)
        label = sentiment[0]['label']
        score = sentiment[0]['score']
        li.append([id, time_line, 'twitter', tweet, label, score])
        count = count = count - 1
        print(count)
        print([time_line, tweet, label, score])

    df = pd.DataFrame(li, columns=['id', 'timeline', 'source', 'message', 'label', 'score'])
    df.reset_index(drop=True, inplace=True)
    write_sentiment_to_db(df)
    #df.to_csv(output_dir + '/' + filename.replace(".json", ".csv"), index=False)


def process_tweet_files(input_dir):
    all_files = glob.glob(input_dir + '/' + "/*")
    print(all_files)
    for filename in all_files:
        extract_sentiment(filename.split('/')[-1])


if __name__ == "__main__":

    while fetch_unprocessed_raw_messages().shape[0] > 0:
        extract_sentiment()


'''
TODO:
process tweets based on the priority of the handle
'''