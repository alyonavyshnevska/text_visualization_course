import os
import pandas as pd
#pd.set_option('display.max_rows', 500)

import datetime as dt
from matplotlib import pyplot as plt
import seaborn as sns
import re
from collections import Counter
import string
import emoji
import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# Files must be in txt format (exactly as they are exported from Whatsapp app)
files_individual = os.listdir('data')


def read_history(file):
    messages = []
    with open('data/{}'.format(file), 'r') as f:
    #     for msg in f.readlines():
    #         if ':' in msg:
    #             match = re.findall('(.\d+.\d+.\d+, \d+:\d+:\d+.) ([a-zA-Z]+): (.*)', msg)
    #             if match:
    #                 messages.append(match)
        messages = re.findall('(.\d+.\d+.\d+, \d+:\d+:\d+.) ([a-zA-Z]+|[a-zA-Z]+ [a-zA-Z]+): (.*)', f.read())

    # for m in messages:
    #     print(m)

    # # Convert list to a dataframe and name columns
    history = pd.DataFrame(messages, columns=['date', 'name', 'msg'])
    history['date'] = history['date'].str[1:-1] #strip brackets
    history['date'] = pd.to_datetime(history['date'], format="%d.%m.%y, %H:%M:%S")
    #history['date1'] = history['date'].apply(lambda x: x.date())
    history['msg_len'] = history['msg'].str.len()

    return history

#
# history = pd.DataFrame
all = []
for file in files_individual:
    loaded_chat = read_history(file)
    all.append(loaded_chat)

history = pd.concat(all).reset_index()

print(history.shape)
# Deleting messages with media
history = history[~history['msg'].str.contains("omitted|end-to-end encryption")]

#clean data
history['msg'] = history['msg'].str.lower()

#value counts
by_names = history.drop(['index', 'date', 'msg_len'], axis=1)
by_names = by_names.groupby('name').agg(lambda x: x.tolist())
# for m in by_names['msg']:
#     print(m)

# v = TfidfVectorizer()
# x = v.fit_transform(by_names)


# text_data = np.array(['I love Brazil. Brazil!',
#                       'Sweden is best',
#                       'Germany beats both'])

text_data = np.array(history['msg'])

# Create the tf-idf feature matrix
tfidf = TfidfVectorizer()
feature_matrix = tfidf.fit_transform(text_data)

# Show tf-idf feature matrix
print(feature_matrix.toarray())

# Show tf-idf feature matrix
print(tfidf.get_feature_names())

print(pd.DataFrame(feature_matrix.toarray(), columns=tfidf.get_feature_names()))
