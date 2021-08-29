from transformers import pipeline
import tensorflow as tf




'''
model='huggingface/distilbert-base-uncased-finetuned-mnli' 
Tensorflow based.
improvise to avoid downloading the models each time


GPU usage:
https://www.tensorflow.org/install/gpu
https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/

'''

def get_sentiment(text):
    seq = pipeline(task = 'text-classification', model='huggingface/distilbert-base-uncased-finetuned-mnli')
    return (str(seq(text)))



def test_case():
    #print(tf.test.gpu_device_name())
    text = 'Bitcoin ATM operators set up association to counter money laundering. This will increase the bitcoin value further'
    print(get_sentiment(text))

if __name__ == "__main__":
    test_case()

