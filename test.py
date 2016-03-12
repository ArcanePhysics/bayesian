from parsing.document import Document, Word
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

	## Example use case
	for doc in docs:
		print doc.words

if __name__ == "__main__":
 	test()