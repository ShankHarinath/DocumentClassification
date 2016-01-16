from parser import Parser
from prediction import Predict
from extraction import Extract

def classification(path):
	Parser.parse(path)
	predict = Predict()
	predict.classfication_split()
	predict.classification_cv(5)

def extraction(file):
	extract = Extract()
	extract.parse_docs(file)

if __name__ == "__main__":
	classification("/Users/Shank/Downloads/training/")
	extraction("/Users/Shank/Downloads/training/positive/Abdominal_defects")