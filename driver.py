from parser import Parser
from prediction import Predict

def main():
	Parser.parse()
	predict = Predict()
	predict.classfication_split()
	predict.classification_cv(5)

if __name__ == "__main__":
	main()