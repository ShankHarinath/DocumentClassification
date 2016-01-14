from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn import metrics
from sklearn import svm
import pickle

text_clf = Pipeline([('vect', CountVectorizer()),
	('tfidf', TfidfTransformer()),
	('clf', SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, n_iter=5, random_state=42)),])

text_clf = Pipeline([('vect', CountVectorizer()),
	('tfidf', TfidfTransformer()), 
	('clf', svm.SVC()),])

pos = open('pos.pkl', 'r')
neg = open('neg.pkl', 'r')

pos_files = pickle.load(pos)
neg_files = pickle.load(neg)

neg_list = neg_files.values()
pos_list = pos_files.values()

X = []
X.extend(neg_list)
X.extend(pos_list)

y = [0] * len(neg_list)
y.extend([1] * len(pos_list))

_ = text_clf.fit(X, y)