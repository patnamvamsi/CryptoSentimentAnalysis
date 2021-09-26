from transformers import pipeline
import torch
import tensorflow as tf
from transformers import AutoTokenizer, AutoModelForSequenceClassification

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
    classifier = pipeline('sentiment-analysis', model='C:\\Dev\\Projects\\CryptoSentimentAnalysis\\models\\sentiment\\finBERT\\')#, device =0
    return (classifier(text))

def test_case():
    #print(tf.test.gpu_device_name())
    text1 = 'Bitcoin ATM operators set up association to counter money laundering. This will increase the bitcoin value further'
    text2 = '@mcuban Mark, lets chat about crypto, dallas mavs, and shark tank in an interview?'
    #print(get_sentiment([text1,text2]))
    print(get_financial_sentiment([text1,text2]))


if __name__ == "__main__":
    test_case()
