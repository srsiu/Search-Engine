import nltk
import re

class Query:
	def __init__(self, query):
		self.query = query
		self.term_f = {}
		self.tokens = []

	def create_tokens(self):
		self.query.strip()
		self.query = self.query.lower()
		self.query = re.sub(r'[^a-zA-Z0-9 ]+', '', self.query)
		self.tokens = nltk.word_tokenize(self.query)

	def get_freq(self):
		for word in self.tokens:
			if word in self.term_f:
				self.term_f[word] += 1
			else:
				self.term_f[word] = 1

	def run_query(self):
		self.create_tokens()
		self.get_freq()

		#for w in self.term_f:
		#	print(w, self.term_f[w])

