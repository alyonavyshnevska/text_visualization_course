from pathlib import Path
from gensim.models import Word2Vec, KeyedVectors
import re
import string
import os
import numpy as np
import tensorflow as tf
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from tensorflow.contrib.tensorboard.plugins import projector


def process_text(filename, split_at):
	''' reads a txt file returns a clean data
	'''
	clean_sentences = []
	stop_words = set(stopwords.words('english'))
	with open(filename, 'r') as f:
		sentences = f.read().split(split_at)
		clean_sentences = clean_data(sentences, clean_sentences, stop_words)

		return clean_sentences

def clean_data(sentences, clean_sentences, stop_words):
	'''Cleans an unprocessed list of strings'''
	for sentence in sentences:
		sentence = sentence.strip()
		sentence = sentence.lower()
		sentence = re.sub(r'\d+', '', sentence)
		sentence = sentence.translate(str.maketrans('', '', string.punctuation)).split()
		sentence = [word for word in sentence if not word in stop_words]

		#stem
		#stemmer = SnowballStemmer("english")
		#sentence = [stemmer.stem(word) for word in sentence]

		#lemmatize words
		lemmatizer = WordNetLemmatizer()
		sentence = [lemmatizer.lemmatize(word) for word in sentence]

		if sentence:
			clean_sentences.append(sentence)

	return clean_sentences



def train_model(input_filename, model_name, split_at):
	# define training data
	sentences = process_text(input_filename, split_at)
	print(sentences)

	# train model
	#model = Word2Vec(sentences, min_count=1)
	model = Word2Vec(sentences, alpha=0.025, size=300, min_alpha=0.025,
					 min_count=1, seed=1, workers=1, iter=50)

	# summarize the loaded model
	#print(model)

	# summarize vocabulary
	words = list(model.wv.vocab)
	# print(words)

	# access vector for one word
	# print(model.wv['life'])

	# save model
	model.save(model_name)

	return model


def load_model(model_name, text_filename, split_at):

	my_file = Path(model_name)
	if my_file.exists():
		model = Word2Vec.load(model_name)
	else:
		model = train_model(text_filename, model_name, split_at)
	return model


def load_keyed_vectors(model_filename):
	'''The trained word vectors are stored in a KeyedVectors instance in model.wv:
	a much smaller and faster object that can be mmapped for lightning fast loading
	and sharing the vectors in RAM between processes'''
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

def save_as_tsv(model):
	'''create a tsv file and a metadata tsv file to visualise vectors'''

	embeddings = {word:vec for word,vec in zip(model.wv.vocab.keys(),
											   model.wv.vectors)}

	embeddings_vectors = np.stack(list(embeddings.values()), axis=0)

	# Create some variables.
	emb = tf.Variable(embeddings_vectors, name='word_embeddings')

	# Add an op to initialize the variable.
	init_op = tf.global_variables_initializer()

	# Add ops to save and restore all the variables.
	saver = tf.train.Saver()

	# Later, launch the model, initialize the variables and save the
	# variables to disk.
	with tf.Session() as sess:
		sess.run(init_op)

		# Save the variables to disk.
		save_path = saver.save(sess, "model_dir/model.ckpt")
		print("Model saved in path: %s" % save_path)

	words = '\n'.join(list(embeddings.keys()))

	with open(os.path.join('model_dir', 'metadata.tsv'), 'w') as f:
		f.write(words)


# .tsv file written in model_dir/metadata.tsv


#load model

monty_text = 'data/monty_python_meaning_of_life.txt'
monty_vectors = 'data/monty_python_model.bin'
monty_sep = '\n'
adams_text = 'data/life_universe.txt'
adams_vectors = 'data/adams_model.bin'
adams_sep = '\n\n'
model = load_model('data/wiki.bin', 'data/wiki.txt', adams_sep)

#load keyed word vectors (smaller in size, not able to train anymore)
#word_vectors = load_keyed_vectors('data/wiki.bin')

# most_similar_list = model.wv.most_similar(positive=['life'], topn=30)
# print(most_similar_list)
# create_word_cloud(most_similar_list)

#X = model[model.wv.vocab]
#visualize_embeddings(X)
#most_similar = output_most_similar(model, 'life', 30)