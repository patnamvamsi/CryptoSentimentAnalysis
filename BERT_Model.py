from transformers import pipeline

'''
model='huggingface/distilbert-base-uncased-finetuned-mnli' 
Tensorflow based.
improvise to avoid downloading the models each time


GPU usage:
https://www.tensorflow.org/install/gpu
https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/

'''

def get_sentiment(text):
    #seq = pipeline(task = 'text-classification', model='huggingface/distilbert-base-uncased-finetuned-mnli')
    seq = pipeline(task = 'sentiment-analysis', model='huggingface/distilbert-base-uncased-finetuned-mnli')
    print(seq.binary_output)
    return (str(seq(text)))

def get_financial_sentiment(text):
    #finBert: https://huggingface.co/ProsusAI/finbert
    #classifier = pipeline('sentiment-analysis', model='ProsusAI/finbert')
    classifier = pipeline('sentiment-analysis', model='../models/sentiment/finBERT/')#, device =0
    return (classifier(text))

def test_case():
    #print(tf.test.gpu_device_name())
    text1 = 'Bitcoin ATM operators set up association to counter money laundering. This will increase the bitcoin value further'
    text2 = '@mcuban Mark, lets chat about crypto, dallas mavs, and shark tank in an interview?'
    #print(get_sentiment([text1,text2]))
    print(get_financial_sentiment([text1,text2]))


if __name__ == "__main__":
    test_case()


## Requirements:
'''
Config:
Must Have:
1. make the batch size configurable
2. model should be configurable
3. prioritising the processing should be configurable
4. 



Good to have:
1. in future make it dynamic to figureout the batch size
2. 


Background processes:
1. get the latest trends in the crypto world and send to webserver
2. get the latest news and calculate Sentiment, store it in a DB

3. Lookup reddit forums for the latest news\ threads. Get the top discussing forums 
    1. send back the title and the link
    2. analyse the sentiment of the thread

4. prioritize #1,#2 from above then below --  batch based. -- Make it configurable 

*** on stoping the server, stop the batch , close the DB connections and shut down ***

API interface:
1. Analyse sentiment for a given twitter handle -- (submit)
    1. fetch  entire timeline from twitter, store the raw json
    2. extract relevent fields from the json and store it in relational DB
    3. analyse sentiment using BERT, batch wise, and update the table
    4. send back the progress of the status -- OR can it be done via DB
    
2. Analyse sentiment for a given hastag. -- (submit)
    1. Get highest trending tweets\ retweets \ replies for the given hashtag
    2. same as above #2
    3. same as above #3
    4. send back the progress of the status -- OR can it be done via DB
    
3. For already processed tweet\hastag, return timeline,tweet and sentiment
    based on from \ to dates
    Inputs: 1.  hastag\ tweeterhandle
            2. from data and to date
    Outputs: timeline , tweet and sentiment
    
4. aggregate sentiment for a given twitter handle or a hashtag



'''