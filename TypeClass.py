import string
from copy import deepcopy


class Type(object):
	def __init__(self, document, name):
		self.name = name
		self.words = {}
		self.numDocuments = 1
		for word in document.words.iteritems()
			if word in self.words:
			else:
				tmp = deepcopy word;
				tmp.probability = 1
				self.words[ word.text ] = tmp
	def train(self, document):
		self.numDocuments++
		for word in document.words.iteritems()
			if word in self.words:
				self.words[ word.text ].probability = (self.words[word.text].probability * (numDocuments - 1) + 1 ) / self.numDocuments
			else:
				tmp = deepcopy word
				tmp.Probability = 1 / self.numDocuments
				self.words[ word.text ] = tmp
	def getProb(self, word):
		if word in self.words:
			return self.words[ word.text ].probability
		else:
			return 0

def test():
	

if __name__ == "__main__":
 	test()
