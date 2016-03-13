import string
from parsing.document import Document, Word
from copy import deepcopy


class Type(object):
	def __init__(self, document, name):
		self.name = name
		self.words = {}
		self.numDocuments = 1
		for _, word in document.words.iteritems():
			if word.text not in self.words.keys():
				tmp = deepcopy(word)
				tmp.probability = 1.0
				self.words[word.text] = tmp

	def train(self, document):
		for _, word in self.words.iteritems():
			word.probability = word.probability * self.numDocuments / (self.numDocuments + 1)
		self.numDocuments = self.numDocuments + 1
		for _, word in document.words.iteritems():
			#print "Checking ", word.text
			#print word.text, " already exists in ", self.name, ": ", word.text in self.words.keys()
			if word.text in self.words.keys():
                                #print "Updating ", word.text
                                #print "Prior probability ", self.words[word.text].probability
                                self.words[word.text].probability = self.words[word.text].probability + 1.0 / self.numDocuments
                                #print "Posterior probability ", self.words[word.text].probability
                        else:
                                #print "Adding ", word.text
                                tmp = deepcopy(word)
				tmp.probability = 1.0 / self.numDocuments
                                self.words[word.text] = tmp
                                #print "Posterior probability ", self.words[word.text].probability
	def getProb(self, word):
		if word in self.words:
			wordObj = self.words[word]
			return wordObj.probability
		else:
			return 0
	def test(self, document):
		likelihood = 0.0
		for _, word in document.words.iteritems():
                        #print word.text, " probability: ", self.getProb(word.text)
			likelihood = likelihood + self.getProb(word.text)
			#print "likelihood: ", likelihood
		return likelihood
