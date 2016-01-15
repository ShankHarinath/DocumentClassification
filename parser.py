import os
import codecs
import pickle
from bs4 import BeautifulSoup

class Parser:
	
	@staticmethod
	def read_files(dir_name, class_type, dump_name):
		files = {}
		fp = open(dump_name, 'w')
		dir = dir_name

		for file in os.listdir(dir+class_type):
			if file == ".DS_Store":
				continue
			print(file)
			soup = BeautifulSoup(codecs.open(dir + class_type + "/" + file, encoding='utf8'), "html5lib")
			files[str(file)] = soup.get_text()

		fp = open(dump_name, 'w')
		pickle.dump(files, fp)

	@staticmethod
	def parse():
		dir = "/Users/Shank/Downloads/training/"
		read_files(dir, 'positive', 'pos1.pkl')
		read_files(dir, 'negative', 'neg.pkl')