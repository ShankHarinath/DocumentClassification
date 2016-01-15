from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import cross_validation
from sklearn.cross_validation import train_test_split
import pickle
import numpy as np
from numpy import array

class Predict:

	def __init__(self):
		pos_list = pickle.load(open('pos.pkl', 'r')).values()
		neg_list = pickle.load(open('neg.pkl', 'r')).values()

		self.X = []
		self.X.extend(neg_list)
		self.X.extend(pos_list)


		self.y = [0] * len(neg_list)
		self.y.extend([1] * len(pos_list))

		self.train, self.test, self.tr_labels, self.te_labels = train_test_split(self.X, self.y, test_size=0.20, random_state=57)
		
		self.y = array(self.y)
		self.X = array(self.X)

		self.model_builder = Pipeline([('counts', CountVectorizer()),
			('tf-idf', TfidfTransformer()),
			('classifier', SGDClassifier(loss='hinge', penalty='l2', alpha=1e-4, n_iter=20, verbose=1, random_state=57)),])
		
	def classification_cv(self, fold):
		cv = cross_validation.KFold(len(self.X), n_folds=fold)
		res = []

		for tr, te in cv:
			_ = self.model_builder.fit(self.X[tr], self.y[tr])
			predicted = self.model_builder.predict(self.X[te])
			res.append(np.mean(predicted == self.y[te]))

		print(str(fold) + "-fold cross validation:")
		print(res)

	def classfication_split(self):
		_ = self.model_builder.fit(self.train, self.tr_labels)
		predicted = self.model_builder.predict(self.test)
		print("80-20 split accuracy:" + np.mean(predicted == self.te_labels))



