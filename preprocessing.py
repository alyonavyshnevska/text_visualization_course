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
    print(file)
    loaded_chat = read_history(file)
    all.append(loaded_chat)

for m in all:
    print(m['name'])

history = pd.concat(all).reset_index()

print(history.shape)
# Deleting messages with media
history = history[~history['msg'].str.contains("omitted")]

#clean data
history['msg'] = history['msg'].str.lower()

#value counts
print(history.groupby(['name']).groups.keys())
#
# history_by_name = history.groupby('name')['msg']
# #print(history_by_name.groups)
#
# v = TfidfVectorizer()
# x = v.fit_transform(history['msg'])
#
# #print(x)

