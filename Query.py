import nltk

class Query:
	def __init__(self, query):
		self.query = query

	def create_tokens(self):
		tokens = nltk.word_tokenize(query)