from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn import metrics
from sklearn import svm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import pickle
import numpy as np

text_clf = Pipeline([('vect', CountVectorizer()),
	('tfidf', TfidfTransformer()),
	('clf', SGDClassifier(loss='hinge', penalty='l2', alpha=1e-4, n_iter=20, verbose=1, random_state=57)),])

pos = open('pos.pkl', 'r')
neg = open('neg.pkl', 'r')

pos_files = pickle.load(pos)
neg_files = pickle.load(neg)

neg_list = neg_files.values()
pos_list = pos_files.values()

train = []
train.extend(neg_list[1:8000])
train.extend(pos_list[1:2953])

test = []
test.extend(neg_list[8000:])
test.extend(pos_list[2953:])

tr_labels = [0] * len(neg_list[1:8000])
tr_labels.extend([1] * len(pos_list[1:2953]))

te_labels = [0] * len(neg_list[8000:])
te_labels.extend([1] * len(pos_list[2953:]))

text_clf.fit(train, tr_labels)

predicted = text_clf.predict(test)
print(np.mean(predicted == te_labels))
