import nltk
import re
import retrieval
import math

class Query:
	def __init__(self, query):
		self.query = query
		self.term_f = {}
		self.tokens = []
		self.retr_info = retrieval.Retrieval()
		self.tfidf_dict = {}

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

	def calc_td_idf(self, word):
		tf = term_f[word] / len(tokens)
		idf = math.log10(self.retr_info.total_docs / self.retr_info.get_doc_freq(word))

		tf_idf = tf * idf
		return tf_idf

	def calc_all_tdidf(self):
		for t in term_f:
			self.tfidf_dict[t] = self.calc_td_idf(t)



