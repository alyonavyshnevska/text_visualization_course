import pandas as pd
import re
import nltk
from nltk.stem.snowball import SnowballStemmer


def read_history(file):
    with open('data/{}'.format(file), 'r') as f:
        messages = re.findall('(.\d+.\d+.\d+, \d+:\d+:\d+.) ([a-zA-Z]+|[a-zA-Z]+ [a-zA-Z]+): (.*)', f.read())

    # # Convert list to a dataframe and name columns
    history = pd.DataFrame(messages, columns=['date', 'name', 'msg'])
    history['date'] = history['date'].str[1:-1]     # strip brackets
    history['date'] = pd.to_datetime(history['date'], format="%d.%m.%y, %H:%M:%S")
    history['date'] = history['date'].apply(lambda x: x.date())
    history['msg_len'] = history['msg'].str.len()

    return history


def tokenize_and_stem(text):

    stemmer = SnowballStemmer("english")

    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    stems = [stemmer.stem(t) for t in filtered_tokens]
    return stems
