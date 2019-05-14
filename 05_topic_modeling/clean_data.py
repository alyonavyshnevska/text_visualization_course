from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem.wordnet import WordNetLemmatizer
from gensim.models.ldamodel import LdaModel as ldamodel
from gensim import corpora, models
import pandas as pd
import gensim
import pprint
from gensim.test.utils import datapath
import pyLDAvis
import pyLDAvis.gensim

stop_words = stopwords.words('english')
stop_words.extend(['content', 'context', 'number', 'file', 'yet', 'user', 'year', 'name', 'column', 'row',
                   'dataset', 'data', 'database', 'from', 'subject', 're',
                   'edu', 'use', 'not', 'would', 'say',
                   'could', '_', 'be', 'know', 'good', 'go', 'get', 'do', 'done',
                   'try', 'many', 'some', 'nice', 'thank', 'think', 'see', 'rather',
                   'easy', 'easily', 'lot', 'lack', 'make', 'want', 'seem', 'run', 'need',
                   'even', 'right', 'line', 'even', 'also', 'may', 'take', 'come'])


pattern = r'\b[^\d\W]+\b'
tokenizer = RegexpTokenizer(pattern)
lemmatizer = WordNetLemmatizer()

# Input from csv
df = pd.read_csv('voted-kaggle-dataset.csv')

# sample data
#print(df['Description'].head())

# list for tokenized documents in loop
texts = []

# loop through document list
for i in df['Description'].iteritems():
    # clean and tokenize document string
    raw = str(i[1]).lower()
    tokens = tokenizer.tokenize(raw)

    # remove stop words from tokens
    stopped_tokens = [raw for raw in tokens if raw not in stop_words]

    # lemmatize tokens
    lemma_tokens = [lemmatizer.lemmatize(toks) for toks in stopped_tokens]

    # remove word containing only single char
    new_lemma_tokens = [raw for raw in lemma_tokens if len(raw) > 1]

    # add tokens to list
    texts.append(new_lemma_tokens)

# sample data
#print(len(texts))

# turn our tokenized documents into a id <-> term dictionary
dictionary = corpora.Dictionary(texts)
# convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in texts]

lda_model = ldamodel(corpus, num_topics=15, id2word = dictionary, passes=20)
pprint.pprint(lda_model.top_topics(corpus,topn=5))

# # Save model to disk.
temp_file = datapath("model")
# model.save(temp_file)

# Load a potentially pretrained model from disk.
# lda = ldamodel.load(temp_file)

print(lda_model.show_topics())

prepared = pyLDAvis.gensim.prepare(lda_model, corpus, dictionary)
pyLDAvis.show(prepared)
pyLDAvis.prepared_data_to_html(prepared, 'vis_topic_model_01.html')
# pyLDAvis.display(vis_data)