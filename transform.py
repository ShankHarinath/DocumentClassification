import numpy as np
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

pos = open('pos.pkl', 'r')
neg = open('neg.pkl', 'r')

pos_files = pickle.load(pos)
neg_files = pickle.load(neg)

neg_list = neg_files.values()
pos_list = pos_files.values()

neg_vect = CountVectorizer()
neg_counts = neg_vect.fit_transform(neg_list)

pos_vect = CountVectorizer()
pos_counts = pos_vect.fit_transform(pos_list)

tf_neg = TfidfTransformer().fit_transform(neg_counts)
tf_pos = TfidfTransformer().fit_transform(pos_counts)

