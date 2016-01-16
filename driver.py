from parser import Parser
from prediction import Predict
from extraction import Extract

def classification():
	Parser.parse()
	predict = Predict()
	predict.classfication_split()
	predict.classification_cv(5)

def extraction():
	extract = Extract()
	extract.parse_docs("/Users/Shank/Downloads/training/positive/Abdominal_defects")

if __name__ == "__main__":
	classification()
	extraction()