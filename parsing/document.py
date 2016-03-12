import string

class Word(object):
	def __init__(self, text):
		self.text = text
		self.tag = None
		self.frequency = 1
		self.probability = 0

	def __repr__(self):
		return "%s (%s, %d, %f)" % (self.text, self.tag, self.frequency, self.probability)

class Document(object):

	def __init__(self):
		self._rawData = []
		self.words = {}

	@staticmethod
	def _parseFile(fileName):
		f = open(fileName)
		text = f.read().lower()
		return Document._preprocessArray(text.split())

	@staticmethod
	def _preprocessWord(word):
		preprocess = lambda w: w.strip(string.punctuation).lower()
		return preprocess(word).strip()

	@staticmethod
	def _preprocessArray(stringArray):
		r = []
		for w in stringArray:
			w = Document._preprocessWord(w)
			if len(w) > 0:
				r.append(w)
		return r

	def initFromFile(self, fileName):
		self._rawData = Document._parseFile(fileName)
		self._initWords()

	def initFromArray(self, stringArray):
		self._rawData = Document._preprocessArray(stringArray)
		self._initWords()

	def _initWords(self):
		self.words = {}
		for w in self._rawData:
			if w in self.words:
				self.words[w].frequency = self.words[w].frequency + 1
			else:
				self.words[w] = Word(w)


def test():
	ar = ["hello", "World,", "Sup", "dude;", "232145", "", "   ", "gg", "hello", "Hello", "wOrlD"]
	d = Document()
	d.initFromArray(ar)
	print d._rawData

	## Example use case
	for (key, obj) in d.words.iteritems():
		print obj
		# obj.probability <- get/set probability

if __name__ == "__main__":
 	test()
