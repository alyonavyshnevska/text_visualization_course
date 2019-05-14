from gensim.models.ldamodel import LdaModel as ldamodel
from gensim import corpora
import pprint
from gensim.test.utils import datapath
import pyLDAvis
import pyLDAvis.gensim
from clean_data import clean as clean

def train_model(texts):

    # turn our tokenized documents into a id <-> term dictionary
    dictionary = corpora.Dictionary(texts)
    # convert tokenized documents into a document-term matrix
    corpus = [dictionary.doc2bow(text) for text in texts]

    # Load a potentially pretrained model from disk.
    if ldamodel.load(datapath("model")):
        lda_model = ldamodel.load(datapath("model"))

    else:
        # train model
        lda_model = ldamodel(corpus, num_topics=10, id2word=dictionary)
        pprint.pprint(lda_model.top_topics(corpus, topn=5))

        # Save model to disk.
        temp_file = datapath("model")
        lda_model.save(temp_file)

    return lda_model, corpus, dictionary


def visualize_pyldavis(lda_model, corpus, dictionary):
    prepared = pyLDAvis.gensim.prepare(lda_model, corpus, dictionary)
    pyLDAvis.save_html(prepared, 'vis_topic_model_01.html')
    pyLDAvis.show(prepared)


if __name__ == '__main__':

    #list of docs as lists of strings
    texts = clean('voted-kaggle-dataset.csv')

    lda_model, corpus, dictionary = train_model(texts)
    # print(lda_model.show_topics())

    visualize_pyldavis(lda_model, corpus, dictionary)