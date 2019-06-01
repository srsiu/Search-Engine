import json
import os
import re
import sys
import math
import operator
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
        file_path = os.path.join('.', 'WEBPAGES_RAW', 'bookkeeping.json')
        self.webpage_dict = json.load(open(file_path), encoding="utf-8")

        with open('total_num_docs.txt', 'r') as doc:
        	self.total_docs = int(doc.read())
        
    def calculate_cosine(self, tfidf_dict):
        # for each term
        # for each doc that includes that term
        for term in tfidf_dict:
            for x in range(0, len(self.invert_ind[term])):
                docID = self.invert_ind[term][x]["docID"]
                tag = self.invert_ind[term][x]["html_tags"]
                j = 0
                if docID in self.scores:
                	if tag == 1:
                		j = .25
                	self.scores[docID] += (self.invert_ind[term][x]["tf-idf"] * tfidf_dict[term] ) + j
                else:
                	if tag == 1:
                		j = .25
                	self.scores[docID] = (self.invert_ind[term][x]["tf-idf"] * tfidf_dict[term] ) + j
                    
        for docID in self.scores:
            self.scores[docID] = self.scores[docID] / self.doc_l[docID]
    
    def get_top_results(self):
        sorted_list = sorted(self.scores.items(), key=lambda x: x[1], reverse=True)
        sorted_dict = dict(sorted_list)
        return sorted_dict

    def print_inverted_ind(self):
        for term, l in self.invert_ind.items():
            print(term, ":", l)

    def get_doc_freq(self, word):
    	return len(self.invert_ind[word])
 
    def print_scores(self):
        print("SCORES\n")
        for docID in self.scores:
            print(docID, ":", self.scores[docID])
            
    def get_top_web_results(self):
        length = 0
        for docID in self.scores:
            if self.scores[docID] != 0:
                length += 1
        i = 1
        for docID in self.scores:
            print("Number of results: ", length)
            print(i,self.webpage_dict[docID])
            i += 1
            if i > 21:
                break


if __name__ == '__main__':
    sys.stdout = open("retrieval_out.txt", "w")  # OUTPUT to file called output.txt
    i = Retrieval()
    i.print_inverted_ind()
