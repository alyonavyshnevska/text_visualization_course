from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem.wordnet import WordNetLemmatizer
import pandas as pd


def clean(filename):

    stop_words = stopwords.words('english')
    stop_words.extend(['content', 'context', 'number', 'file', 'yet', 'user', 'year', 'name', 'column', 'row',
                       'dataset', 'datasets', 'data', 'database', 'from', 'subject', 're', 'numeric', 'integer', 'strongly', 'csv',
                       'edu', 'use', 'not', 'would', 'say', 'text', 'contains', 'file',
                       'could', '_', 'be', 'know', 'good', 'go', 'get', 'do', 'done', 'made', 'highly', 'numerical',
                       'try', 'many', 'some', 'nice', 'thank', 'think', 'see', 'rather',
                       'easy', 'easily', 'lot', 'lack', 'make', 'want', 'seem', 'run', 'need',
                       'even', 'right', 'line', 'even', 'also', 'may', 'take', 'come'])


    pattern = r'\b[^\d\W]+\b'
    tokenizer = RegexpTokenizer(pattern)
    lemmatizer = WordNetLemmatizer()

    # Input from csv
    df = pd.read_csv(filename)

    #Only model first 100 docs
    df = df['Description'][:100]

    texts = []

    # loop through document list
    for i in df.iteritems():
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

    return texts

print('hello')
for i in range(1,10):
    print(i)