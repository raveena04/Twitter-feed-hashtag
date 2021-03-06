from google.colab import drive
drive.mount('/content/gdrive')

#import glove
!pip install glove-python

# we need to pass splitted sentences to the model
import nltk,csv,numpy
nltk.download('punkt')
from nltk import sent_tokenize, word_tokenize, pos_tag
sentences=[]
reader = csv.reader(open('/content/gdrive/My Drive/itw practicals/ua.csv', 'rU'), delimiter= ",",quotechar='|')
for line in reader:
    for field in line:
      sentences.append(word_tokenize(field))
print(sentences)
lines=sentences

#importing the glove library
from glove import Corpus, Glove

# creating a corpus object
corpus = Corpus() 

#training the corpus to generate the co occurence matrix which is used in GloVe
corpus.fit(lines, window=10)

glove = Glove(no_components=30, learning_rate=0.05)
 
glove.fit(corpus.matrix, epochs=30, no_threads=4, verbose=True)
glove.add_dictionary(corpus.dictionary)
glove.save('glove2582020.model')

import warnings
warnings.filterwarnings('ignore')
from gensim.models.word2vec import Word2Vec
import gensim.downloader as api

!wget http://nlp.stanford.edu/data/glove.6B.zip

!unzip glove*.zip

import numpy as np

print('Indexing word vectors.')

embeddings_index = {}
f = open('glove.6B.100d.txt', encoding='utf-8')
for line in f:
    values = line.split()
    word = values[0]
    coefs = np.asarray(values[1:], dtype='float32')
    embeddings_index[word] = coefs
f.close()

print('Found %s word vectors.' % len(embeddings_index))

from gensim.test.utils import datapath, get_tmpfile
from gensim.models import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec

glove_file = datapath('/content/glove.6B.100d.txt')
word2vec_glove_file = get_tmpfile("glove.6B.100d.word2vec.txt")
glove2word2vec(glove_file, word2vec_glove_file)

model = KeyedVectors.load_word2vec_format(word2vec_glove_file)

model.most_similar('post')

result = model.most_similar(positive=['post', 'tweet'])
print("{}: {:.4f}".format(*result[0]))

