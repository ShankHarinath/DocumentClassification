import os
import codecs
import pickle
from bs4 import BeautifulSoup

pos_files = {}
dir = "/Users/Shank/Downloads/training/positive"

for file in os.listdir(dir):
	print(file)
	soup = BeautifulSoup(codecs.open(dir+"/"+file, encoding='utf8'), "html5lib")
	pos_files[str(file)] = soup.get_text()

pos = open('pos.pkl', 'wb')
pickle.dump(pos_files, pos)

neg_files = {}
dir = "/Users/Shank/Downloads/training/negative"

for file in os.listdir(dir):
	print(file)
	soup = BeautifulSoup(codecs.open(dir+"/"+file, encoding='utf8'), "html5lib")
	neg_files[str(file)] = soup.get_text()

neg = open('neg.pkl', 'wb')
pickle.dump(neg_files, neg)