import string
from parsing.document import Document, Word
from TypeClass import Type
from copy import deepcopy


class Bayesian(object):
	def __init__(self):
                self.types = []
                self.numTypes = 0
        def train(self, document, typename):
                if self.numTypes == 0:
                        self.types.append(Type(document, typename))
                        #print "Added first type ", typename, " with 1 new document "
                        self.numTypes = self.numTypes + 1
                else:
                        found = False
                        for t in self.types:
                                if t.name == typename:
                                        #print "Found type ", typename, " in identifier"
                                        t.train(document)
                                        #print "Updateted type ", typename, " with a new document"
                                        found = True
                                        break
                        if not found:
                                #print "Didn't find type ", typename, " in identifier"
                                self.types.append(Type(document, typename))
                                #print "Added type ", typename, " with 1 new document "
        def identify(self, document):
                bestScore = 0
                for t in self.types:
                        score = t.test(document)
                        #print "Testing for type", t.name
                        #print "Score =", score
                        if score > bestScore:
                                bestType = t
                                #print "Current best type is:", t.name
                return bestType.name
                
		
