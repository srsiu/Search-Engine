import json
import os
import re
import sys
import math
import itertools

from collections import defaultdict
from urllib.parse import urlparse

import lxml.etree
import lxml.html
from bs4 import BeautifulSoup
from nltk.corpus import stopwords

import corpus
import html_parse


class Retrieval:
    def __init__(self):
        self.scores = dict()
        self.invert_ind = json.load(open("inverted_index.json"), encoding="utf-8")
        
    def calculate_cosine(self, query_tf_idf):

        for term in self.invert_ind:
            for x in range(0, len(self.invert_ind[term])):
                self.scores[term] = (self.invert_ind[term][x]["tf-idf"] +
                                     query_tf_idf) / len(self.invert_ind[term][x])
        return sorted(self.invert_ind.items(), key=lambda x:)
    def get_top_results(self, L):
        x = itertools.islice(L.items(), 0, 9)
        return x

    def print_inverted_ind(self):
        for term, l in self.invert_ind.items():
            print(term, ":", l)

if __name__ == '__main__':
    sys.stdout = open("retrieval_out.txt", "w")  # OUTPUT to file called output.txt
    i = Retrieval()
    i.print_inverted_ind()
