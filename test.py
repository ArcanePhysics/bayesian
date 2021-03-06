from parsing.document import Document, Word
from TypeClass import Type
from BayesianClass import Bayesian
from os import path

def test():
	a = ['a', 'bb', 'gg']
	b = ['bb', 'c']

	d1 = Document()
	d2 = Document()
	d1.initFromArray(a)
	d2.initFromArray(b)

	t = Type( d1, 'test' )
	print t.words
	
	t.train(d2)

	print t.words

	test_dir = 'tests'
	test_files = ['test1', 'test2', 'test3', 'test4', 'test5', 'test6', 'test7', 'test8', 'test9', 'test10']

	docs = []
	for testFile in test_files:
		p = path.join( test_dir, testFile )
		d = Document()
		d.initFromFile(p)
		docs.append(d)

	spam = Type( docs[0], 'spam' )

	for d in docs[1:5]:
		spam.train(d)

	print spam.getProb( 'a' )

	print spam.test(docs[1])

	bayesian = Bayesian()
	bayesian.train(docs[0], "spam")
	bayesian.train(docs[1], "spam")
	bayesian.train(docs[2], "non-spam")
	bayesian.train(docs[3], "non-spam")
	print bayesian.identify(docs[4])

if __name__ == "__main__":
 	test()
