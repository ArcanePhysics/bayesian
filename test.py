from parsing.document import Document, Word
from TypeClass import Type
from os import path

def test():
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

	print spam.getProb( 'people' )

if __name__ == "__main__":
 	test()