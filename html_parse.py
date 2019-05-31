import json
import os
import re
import sys
import math
from collections import defaultdict
from urllib.parse import urlparse

import lxml.etree
import lxml.html
from bs4 import BeautifulSoup
from nltk.corpus import stopwords

import corpus




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
        file_path = os.path.join('.', 'WEBPAGES_RAW', 'bookkeeping.json')
        self.webpage_dict = json.load(open(file_path), encoding="utf-8")
        
        '''JSON Format   "0/0" : "www.uci.edu" '''


    def create_index(self, tf, folder, invert_ind, metadata):
        for term in tf:
            if term in invert_ind:
                invert_ind[term].append({"freq":tf[term], "docID":folder, "metadata":metadata, "tf-idf":0 })
                #print("appended", term, folder)
            else:
                invert_ind[term] = [{"freq": tf[term], "docID":folder, "metadata":metadata, "tf-idf":0}]
                #print("added", term, folder)
            
    def html_parse(self):

        corpus_all = corpus.Corpus()
        '''for m in corpus_all.url_file_map:
            print(m)'''
        
        '''docs is a list of set of words in each doc'''
        docs = list()
        '''dictionary intialization'''
        
        tok = Tokenize();

        # FORMAT: { term: [ {freq: #, docID: #}, ...]}
        # Should add - metadata: type (ex: h1, h2, h3, p)

        i = 0
        for folder in self.webpage_dict:
            address = folder.split("/")
            dir = address[0] # Strings
            file = address[1] # Strings
            
            file_name = os.path.join(".", "WEBPAGES_RAW", dir, file)

            print("FILE:", file_name, "|", file, "|", dir)
            
            i += 1
            if i > 12:
                break
            if file_name != None:
                
                self.num_of_documents += 1
                metadata = "p"
                with open(file_name, "r", encoding="utf8") as html_doc:
                    soup = BeautifulSoup(html_doc, "lxml")
                    paragraphs = soup.find_all(metadata)
                    total_string = ""
                    for p in paragraphs:
                        total_string += p.text
                    tf = tok.term_freq(total_string)
                    self.create_index(tf, folder, self.invert_ind, metadata)
                    #for x,y in invert_ind:
                    #print(x,"\t",y)
            
                    
    def calculate_tf_idf(self):
        for term in self.invert_ind:
            self.invert_ind["tf-idf"] = (1 + math.log10(self.invert_ind[term]["freq"])) * \
                math.log10(self.num_of_documents / len(self.invert_ind[term]))    
    
    def print_inverted_ind(self):
        for term, l in self.invert_ind.items():
            print(term, ":", l)
        


"""write main function"""
if __name__ == '__main__':
    sys.stdout = open("output2.txt", "w")  # OUTPUT to file called output.txt
    i = InvertedIndex() 
    i.html_parse()
    i.print_inverted_ind()
    i.calculate_tf_idf()
    i.print_inverted_ind()
    
