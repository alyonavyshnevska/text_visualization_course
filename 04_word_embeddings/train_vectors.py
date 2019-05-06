from pathlib import Path
from gensim.models import Word2Vec
from gensim.models import KeyedVectors
import re
import string
from nltk.corpus import stopwords
from gensim.models import Word2Vec
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

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
		sentence = [word for word in sentence if word not in stop_words]

		#lemmatize words
		lemmatizer = WordNetLemmatizer()
		sentence = [lemmatizer.lemmatize(word) for word in sentence]

		if sentence:
			clean_sentences.append(sentence)

	return clean_sentences



def train_model(input_filename):
	# define training data
	sentences = process_text(input_filename)
	# print(sentences)

	# train model
	model = Word2Vec(sentences, min_count=1)

	# summarize the loaded model
	# print(model)

	# summarize vocabulary
	words = list(model.wv.vocab)
	# print(words)

	# access vector for one word
	# print(model.wv['life'])

	# save model
	model.save('data/monty_python_model.bin')

	return model


def load_model(model_name, text_filename=None):

	my_file = Path(model_name)
	if my_file.exists():
		model = Word2Vec.load(model_name)
	else:
		model = train_model(text_filename)
	return model


def load_keyed_vectors(model_filename):
	word_vectors = KeyedVectors.load(model_filename, mmap='r')
	return word_vectors


def visualize_embeddings(X):
	# fit a 2d PCA model to the vectors
	pca = PCA(n_components=2)
	result = pca.fit_transform(X)

	# create a scatter plot of the projection
	plt.scatter(result[:, 0], result[:, 1])
	words = list(model.wv.vocab)
	for i, word in enumerate(words):
		plt.annotate(word, xy=(result[i, 0], result[i, 1]))
	plt.show()


def create_word_cloud(most_similar_list):
	assert type(most_similar_list) == list

	#list to dict, as needed for wordcloud input
	most_similar_dict = {word:distance for word,distance in most_similar_list}

	#generate wordcloud from frequencies
	wordcloud = WordCloud().generate_from_frequencies(most_similar_dict)

	# Display the generated image:
	plt.imshow(wordcloud, interpolation='bilinear')
	plt.axis("off")
	plt.show()


#load model
#model = load_model('data/monty_python_model.bin', 'data/monty_python_meaning_of_life.txt')

#load keyed word vectors
word_vectors = load_keyed_vectors('data/monty_python_model.bin')
most_similar_list = word_vectors.wv.most_similar(positive=['life'])
print(most_similar_list)
create_word_cloud(most_similar_list)

#X = model[model.wv.vocab]
#visualize_embeddings(X)
#most_similar = output_most_similar(model, 'life', 30)