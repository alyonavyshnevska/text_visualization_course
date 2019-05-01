import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from matplotlib import pyplot as plt
from preprocessing import read_history
from src.emoji_process import create_emoji_matrix


def create_history_dataframe(dir_name, one_year=False):
    # Files must be in txt format (exactly as they are exported from Whatsapp app)
    files_individual = os.listdir(dir_name)

    all = []
    codename_counter = 0
    for file in files_individual[:5]:
        loaded_chat = read_history(file)
        #loaded_chat['chat_number'] = "anonymous {}".format(codename_counter)
        loaded_chat['chat_number'] = codename_counter
        all.append(loaded_chat)
        codename_counter += 1

    history = pd.concat(all).reset_index()

    # Deleting messages with 'media ommitted'or service notifications
    history = history[~history['msg'].str.contains("omitted|end-to-end encryption")]

    # Clean Data
    history['msg'] = history['msg'].str.lower()
    history['date'] = pd.to_datetime(history['date'])
    history['msg'] = history['msg'].str.replace('\d+', '')

    # If only use data of one year
    if one_year == True:
        history = history.loc[(history['date'] > '2018-4-1') & (history['date'] <= '2019-4-1')]

    return history


def export_to_csv_file(filename, dataframe_name):
    dataframe_name.to_csv(filename, sep=';', header=True, float_format='%.6f', index=True,
                         encoding='utf8')


def plot_mean_values(dataframe_name, export_plot=False):

    mean_msg_len = dataframe_name.groupby('name')['msg_len'].mean()
    mean_msg_len.plot(kind='box', color='green', title= 'Lengths of Messages', grid=True)
    plt.show()

    if export_plot == True:
        export_to_csv_file('history_csv.csv', dataframe_name)

    return mean_msg_len


def create_tf_idf_matrix(dataframe_name, groupby_param, cols_to_drop):

    #join all messages by one person into one document
    by_names = dataframe_name.drop(cols_to_drop, axis=1)
    #by_names = by_names.groupby(groupby_param)['msg'].apply(' '.join)

    # Create the tf-idf feature matrix
    with open('docs/german-stopwords.txt') as f:
        german_stopwords = (f.read().split('\n'))

    tfidf = TfidfVectorizer(min_df=3, stop_words=german_stopwords)
    feature_matrix = tfidf.fit_transform(by_names['msg'])

    df = pd.DataFrame(feature_matrix.toarray(), columns = tfidf.get_feature_names())

    #target = by_names[groupby_param].values
    #print(tfidf.get_feature_names())
    #print(feature_matrix.shape)

    return tfidf, feature_matrix, by_names[groupby_param], df


def create_tfidf_data_frame(tfidf,feature_matrix, create_transpose=False):

    #create a data frame from matrix
    df = pd.DataFrame(feature_matrix.toarray(), columns=tfidf.get_feature_names())

    if create_transpose == True:
        df_transposed = df.T
        return df_transposed
    else:
        return df


if __name__ == '__main__':
    history = create_history_dataframe('data', one_year=False)
    #print(history.columns)
    # Plot mean mean lengths of messages
    #plot_mean_values(history, export_plot=False)

    # Create tf_idf feature matrix
    tfidf, feature_matrix = create_tf_idf_matrix(history, 'name', ['index', 'date', 'msg_len', 'chat_number'])

    # Create tf-odf frame from tfidf matrix
    tfidf_data_frame = create_tfidf_data_frame(tfidf, feature_matrix, create_transpose=False)
    print('Top tf-idf score for each person', tfidf_data_frame.max(axis=1))

    # Export tfidf_frame
    # export_to_csv_file('df_tfidf_ger.csv', tfidf_data_frame)

    create_emoji_matrix(history, export_matrix=False)
