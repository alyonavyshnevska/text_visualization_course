import pandas as pd
from collections import Counter
import emoji
from visualize import export_to_csv_file

def extract_emojis(str):
    return ''.join(c for c in str if c in emoji.UNICODE_EMOJI)


def Count_Emojis(df):
    series = df['msg']
    all_words = ""
    for sentence in series:
        all_words += extract_emojis(sentence)
    word_count = Counter(all_words)

    ordered = {}
    ordered['msg'] = []
    for key, number in word_count.most_common()[:50]:
        ordered[key] = []

    for sentence in series:
        sentence_count = Counter(extract_emojis(sentence))

        for word in ordered:
            count = sentence_count[word] if sentence_count[word] else 0
            ordered[word] += [count]
    ordered['msg'] = list(series)
    ordered['date'] = list(df['date'])
    ordered['name'] = list(df['name'])

    return pd.DataFrame(ordered)


def create_emoji_matrix(dataframe_name, export_matrix=False):

    # Counting emojis by message (limited to top50)
    emojis_counts = Count_Emojis(dataframe_name)
    dataframe_name['emoji'] = dataframe_name['msg'].apply(lambda x: extract_emojis(x))
    dataframe_name['len_emoji'] = dataframe_name['emoji'].str.len()

    if export_matrix == True:
        export_to_csv_file('history_csv_emoj2.csv', dataframe_name)
        export_to_csv_file('emojis_counts_top50.csv', emojis_counts.drop('msg',axis=1))
        export_to_csv_file('emojis_counts_top50_nomsg.csv', pd.melt(emojis_counts.drop('msg',axis=1),
                                                                id_vars=['name','date'], var_name='Emojis'))

    return dataframe_name