import nltk
import re
import retrieval
import math
import sys
from nltk.stem import WordNetLemmatizer
#nltk.download('punkt')
# nltk.download('wordnet')

class Query:
	def __init__(self, query):
		self.query = query # string
		self.term_f = {} # {term: freq}
		self.tokens = [] # list of tokens from string 
		self.retr_info = retrieval.Retrieval()
		self.tfidf_dict = {} # {term: tfidf}
		self.lemm = WordNetLemmatizer()
    
	def create_tokens(self):
		self.query.strip()
		self.query = self.query.lower()
        
		self.query = re.sub(r'[^a-zA-Z0-9 ]+', '', self.query)
		self.tokens = nltk.word_tokenize(self.query)

	def get_freq(self):
		for word in self.tokens:
			word = self.lemm.lemmatize(word)
			if word in self.term_f:
				self.term_f[word] += 1
			else:
				self.term_f[word] = 1

	def calc_td_idf(self, word):
		tf = self.term_f[word]
		idf = math.log10(self.retr_info.total_docs / self.retr_info.get_doc_freq(word))

		tf_idf = tf * idf
		return tf_idf

	def calc_all_tdidf(self):
		for t in self.term_f:
			self.tfidf_dict[t] = self.calc_td_idf(t)

	def run_query(self):
		self.create_tokens()
		self.get_freq()
		self.calc_all_tdidf()
		self.retr_info.calculate_cosine(self.tfidf_dict)

		sys.stdout = open("query_results.txt", "w")
		self.retr_info.print_top_results()
		self.retr_info.print_top_web_results()
		#self.retr_info.print_scores()
  
	def run_query_gui(self):
		self.create_tokens()
		self.get_freq()
		self.calc_all_tdidf()
		self.retr_info.calculate_cosine(self.tfidf_dict)

		return self.retr_info.get_top_web_results()
		
