import string
from parsing.document import Document, Word
from copy import deepcopy


class Type(object):
	def __init__(self, document, name):
		self.name = name
		self.words = {}
		self.numDocuments = 1
		for _, word in document.words.iteritems():
			if word not in self.words:
				tmp = deepcopy(word)
				tmp.probability = 1.0
				self.words[word.text] = tmp

	def train(self, document):
		self.numDocuments = self.numDocuments + 1
		for _, word in document.words.iteritems():
			if word in self.words:
				self.words[word.text].probability = (self.words[word.text].probability * (self.numDocuments - 1) + 1 ) / self.numDocuments
			else:
				tmp = deepcopy(word)
				tmp.probability = 1.0 / self.numDocuments
				self.words[ word.text ] = tmp

	def getProb(self, word):
		if word in self.words:
			wordObj = self.words[word]
			return wordObj.probability
		else:
			return 0

if __name__ == "__main__":
	pass
