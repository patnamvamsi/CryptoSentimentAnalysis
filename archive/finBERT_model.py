from transformers import AutoTokenizer, AutoModelForSequenceClassification
import tensorflow as tf
from transformers import pipeline
import torch
import numpy as np

def get_financial_sentiment(text):
    tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
    model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")
    #model = AutoModelForSequenceClassification.from_pretrained("C:\\Dev\\Projects\\CryptoSentimentAnalysis\\models\\sentiment\\finBERT\\pytorch_model.bin")
    MAX_LEN = 160
    class_names = ['negative', 'neutral', 'positive']

    encoded_new = tokenizer.encode_plus(
        text,  # Sentence to encode.
        add_special_tokens=True,  # Add '[CLS]' and '[SEP]'
        max_length=MAX_LEN,  # Pad & truncate all sentences.
        pad_to_max_length=True,
        return_attention_mask=True,  # Construct attn. masks.
        return_tensors='pt',  # Return pytorch tensors.
    )

    # Add the encoded sentence to the list.
    input_idst = (encoded_new['input_ids'])
    attention_maskst = (encoded_new['attention_mask'])

    # Convert the lists into tensors.
    input_idst = torch.cat([input_idst], dim=0)
    attention_maskst = torch.cat([attention_maskst], dim=0)

    new_test_output = model(input_idst, token_type_ids=None,
                            attention_mask=attention_maskst)

    logits = new_test_output[0]
    predicted = logits.detach().numpy()

    # Store predictions
    flat_predictions = np.concatenate(predicted, axis=0)

    # For each sample, pick the label (0 or 1) with the higher score.
    new_predictions = np.argmax(flat_predictions).flatten()

    print (new_predictions)
    print(class_names[new_predictions[0]])


def _get_financial_sentiment(text):
    classifier = pipeline('sentiment-analysis', model='ProsusAI/finbert')
    print(classifier(text))


def test_case():
    print(tf.test.gpu_device_name())
    text = 'Bitcoin ATM operators set up association to counter money laundering. This will increase the bitcoin value further'
    #get_financial_sentiment(text)
    _get_financial_sentiment(text)

test_case()