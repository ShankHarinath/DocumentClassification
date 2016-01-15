import os
import codecs
import pickle
from bs4 import BeautifulSoup

class Parser:
	
	@staticmethod
	def read_files(dir_name, class_type, dump_name):
		files = {}
		fp = open(dump_name, 'wb')
		dir = dir_name

		for file in os.listdir(dir):
			print(file)
			soup = BeautifulSoup(codecs.open(dir + class_type + "/" + file, encoding='utf8'), "html5lib")
			files[str(file)] = soup.get_text()

		fp = open(dump_name, 'wb')
		pickle.dump(files, fp)

	@staticmethod
	def parse():
		dir = "/Users/Shank/Downloads/training/"
		read_files(dir, 'positive', 'pos.pkl')
		read_files(dir, 'negative', 'neg.pkl')