import json
import os
import re
import sys
import math
from collections import defaultdict

import lxml.etree
import lxml.html
from bs4 import BeautifulSoup
from nltk.corpus import stopwords

import html_parse
import itertools
import Query

class Retrieval:
    def __init__(self):
        self.scores = dict() # {docID: score}
        self.doc_l = json.load(open("doc_length.json"), encoding="utf-8")
        self.invert_ind = json.load(open("inverted_index.json"), encoding="utf-8")

        with open('total_num_docs.txt', 'r') as doc:
        	self.total_docs = int(doc.read())
        
    def calculate_cosine(self, tfidf_dict):
        # for each term
        # for each doc that includes that term
        for term in tfidf_dict:
            for x in range(0, len(self.invert_ind[term])):
                docID = self.invert_ind[term][x]["docID"]
                if self.scores[docID] != 0:
                    self.scores[docID] += self.invert_ind[term][x]["tf-idf"] * \
                        tfidf_dict[term]
                else:
                    self.scores[docID] = self.invert_ind[term][x]["tf-idf"] * \
                        tfidf_dict[term]
                    
        for docID in self.scores:
            self.scores[docID] = self.scores[docID] / self.doc_l[docID]
    
    def get_top_results(self, L):
        x = itertools.islice(L.items(), 0, 9)
        return x

    def print_inverted_ind(self):
        for term, l in self.invert_ind.items():
            print(term, ":", l)

    def get_doc_freq(self, word):
    	return len(self.invert_ind[word])


if __name__ == '__main__':
    sys.stdout = open("retrieval_out.txt", "w")  # OUTPUT to file called output.txt
    i = Retrieval()
    i.print_inverted_ind()