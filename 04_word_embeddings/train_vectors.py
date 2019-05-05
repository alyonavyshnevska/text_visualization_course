from gensim.models import Word2Vec
import re
import string
from nltk import sent_tokenize
from nltk.corpus import stopwords

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
		sentence = sentence.translate(str.maketrans('', '', string.punctuation))
		sentence = sent_tokenize(sentence)
		sentence = [w for w in list(sentence) if not w in stop_words]
		if sentence:
			clean_sentences.append(sentence)

	return clean_sentences


# define training data
sentences = process_text('data/monty_python_meaning_of_life.txt')
print(sentences)

# # train model
# model = Word2Vec(sentences, min_count=1)
# # summarize the loaded model
# print(model)
# # summarize vocabulary
# words = list(model.wv.vocab)
# print(words)
# # access vector for one word
# print(model.wv['sentence'])
# # save model
# model.save('data/tiny_model.bin')
# # load model
# new_model = Word2Vec.load('data/tiny_model.bin')
# print(new_model)
#
