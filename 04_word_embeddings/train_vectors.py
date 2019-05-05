from gensim.models import Word2Vec
from gensim.models import KeyedVectors
import re
import string
from nltk import sent_tokenize
from nltk.corpus import stopwords
from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from matplotlib import pyplot

def process_text(filename):
	''' reads a txt file returns a clean data
	'''
	clean_sentences = []
	stop_words = set(stopwords.words('english'))
	with open(filename, 'r') as f:
		sentences = f.read().split('\n')
		clean_sentences = clean_data(sentences, clean_sentences, stop_words)

		return clean_sentences

def clean_data(sentences, clean_sentences, stop_words):
	'''Cleans an unprocessed list of strings'''
	for sentence in sentences:
		sentence = sentence.strip()
		sentence = sentence.lower()
		sentence = re.sub(r'\d+', '', sentence)
		sentence = sentence.translate(str.maketrans('', '', string.punctuation)).split()
		sentence = [w for w in sentence if not w in stop_words]
		#sentence = sent_tokenize(sentence)
		#sentence = sentence.split()
		if sentence:
			clean_sentences.append(sentence)

	return clean_sentences

def visualize_embeddings(X):
	# fit a 2d PCA model to the vectors
	pca = PCA(n_components=2)
	result = pca.fit_transform(X)

	# create a scatter plot of the projection
	pyplot.scatter(result[:, 0], result[:, 1])
	words = list(model.wv.vocab)
	for i, word in enumerate(words):
		pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
	pyplot.show()


# define training data
sentences = process_text('data/monty_python_meaning_of_life.txt')
#print(sentences)

# train model
model = Word2Vec(sentences, min_count=1)
# summarize the loaded model
#print(model)
# summarize vocabulary
words = list(model.wv.vocab)
#print(words)
# access vector for one word
#print(model.wv['life'])
# save model
#model.save('data/monty_python_model.bin')
# load model
#new_model = Word2Vec.load('data/monty_python_model.bin')
#print(new_model)

word_vectors = KeyedVectors.load('data/monty_python_model.bin', mmap='r')
result = word_vectors.wv.most_similar(positive=['life'])
print(result)
#X = model[model.wv.vocab]
#visualize_embeddings(X)
#most_similar = output_most_similar(model, 'life', 30)