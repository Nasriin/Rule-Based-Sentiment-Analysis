import nltk
import sys
sentadr = '/Users/nasrin/Documents/Concordia/Fall2014/NLP/FinalProject/Dec1/sampleSent.txt';
grammaradr = '/Users/nasrin/Documents/Concordia/Fall2014/NLP/FinalProject/Dec1/newGrammar.fcfg'
grammar = nltk.data.load(grammaradr)
print('Grammar defined from '+ grammaradr)
print('Sentences loaded form '+ sentadr) 
parser = nltk.parse.earleychart.FeatureEarleyChartParser(grammar)		

with open(sentadr) as f:
	content = f.read().splitlines()
	for sentence in content:
		try:
			parses = parser.parse(sentence.split())
			print(sentence)
			trees = parses.__iter__()
#			print(len(list(trees)))
			for tree in trees:
				tree.draw()
		except StopIteration:
			print("There is no parse tree");
f.close()    
print('END :D')