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


### TOKENIZING ###
class Tokenize:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        
    def rem(self, Li:list):
        ''' Splits the input if its an alphanum, and removes all the extra symbols, returns a list
            Complexity: O(N) since it there is only one loop, and splitting the string and checking if its alphanum
        '''
        pat ="[a-zA-Z0-9']+"
        return re.findall(pat,Li)

    def length(self,word):
   		return len(self.rem(word))

    def make_dict(self, L: list):
        ''' Makes a dictionary with a key of the word and value of the number of occurrences
            returns the dictionary
            Complexity: O(N) since it there is only one loop looping through the list
        '''
        d = {}
        for word in L:
            if word not in self.stop_words:
                if word not in d:
                    d[word]=1
                else:
                    d[word]+=1
        return d

    def term_freq(self, total_string):
        token_list = self.rem(total_string)
        t_freq = self.make_dict(token_list)
        return t_freq
    
### --------- ###

class InvertedIndex:

    def __init__(self):
        self.num_of_documents = 0
        self.invert_ind = dict([])
        self.doc_length = dict()
        file_path = os.path.join('.', 'WEBPAGES_RAW', 'bookkeeping.json')
        self.webpage_dict = json.load(open(file_path), encoding="utf-8")
        self.scores = dict()
        '''JSON Format   "0/0" : "www.uci.edu" '''

    def create_index(self, tf, folder, invert_ind, html_tags):
        for term in tf:
            if term in invert_ind:
                invert_ind[term].append(
                    {"docID": folder, "freq": tf[term], "html_tags": html_tags, 
                     "tf-idf": 0})
            else:
                invert_ind[term] = [
                    {"docID": folder, "freq": tf[term], "html_tags":html_tags, 
                     "tf-idf": 0}]
            
    def html_parse(self):
        tok = Tokenize()

        # FORMAT: { term: [ {freq: #, docID: #}, ...]}
        # Should add - html_tags: type (ex: h1, h2, h3, p)

        i = 0 # Remove after finishing testing
        for folder in self.webpage_dict:
            address = folder.split("/")
            dir = address[0] # Strings
            file = address[1] # Strings
            
            file_name = os.path.join(".", "WEBPAGES_RAW", dir, file)

            #print("FILE:", file_name, "|", file, "|", dir)
            #i += 1
            #if i > 12:
            #    break
            if file_name != None:
                
                self.num_of_documents += 1
                html_tags = "p"
                with open(file_name, "r", encoding="utf8") as html_doc:
                    soup = BeautifulSoup(html_doc, "lxml")
                    paragraphs = soup.find_all(html_tags)
                    total_string = ""
                    for p in paragraphs:
                        total_string += p.text
                    self.doc_length[folder] = tok.length(total_string)
                    tf = tok.term_freq(total_string)
                    self.create_index(tf, folder, self.invert_ind, html_tags)

    def calculate_tf_idf(self, tf, tid,  N, df):
        return (tf/tid * math.log10(N / df))

    def calculate_all_tf_idf(self):
        for term in self.invert_ind:
            for x in range(0, len(self.invert_ind[term])):
                #print("doc: ", doc["docID"], " ", self.invert_ind[term][0]["tf-idf"])
                self.invert_ind[term][x]["tf-idf"] = self.calculate_tf_idf(
                    self.invert_ind[term][x]["freq"], self.doc_length[self.invert_ind[term][x]["docID"]],
                    self.num_of_documents, len(self.invert_ind[term]))

    def print_inverted_ind(self):
        for term, l in self.invert_ind.items():
           print(term, ":", l)
           
    def write_inverted_ind(self):
        with open('inverted_index.json', 'w') as j:
            json.dump(self.invert_ind, j)

    def write_total_docs(self):
    	with open('total_num_docs.txt', 'w') as k:
    		k.write(str(self.num_of_documents))
      
    def write_doc_length(self):
        with open('doc_length.json', 'w') as d:
            json.dump(self.doc_length, d)

"""write main function"""
if __name__ == '__main__':
    sys.stdout = open("output2.txt", "w")  # OUTPUT to file called output.txt
    i = InvertedIndex() 
    i.html_parse()
    i.calculate_all_tf_idf()
    i.print_inverted_ind()
