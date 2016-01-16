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

		for file in os.listdir(dir+class_type):
			if file == ".DS_Store":
				continue
			print(file)
			soup = BeautifulSoup(codecs.open(dir + class_type + "/" + file, encoding='utf8'), "html5lib")
			files[str(file)] = soup.get_text()

		with open(dump_name, 'wb') as handle:
			pickle.dump(files, handle)

	@staticmethod
	def parse(path):
		dir = path
		Parser.read_files(dir, 'positive', 'pos1.pkl')
		Parser.read_files(dir, 'negative', 'neg.pkl')