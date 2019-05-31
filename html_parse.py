import json
import os
import re
import sys
from collections import defaultdict
from urllib.parse import urlparse

import lxml.etree
import lxml.html
from bs4 import BeautifulSoup
from nltk.corpus import stopwords

import corpus

stop_words = set(stopwords.words('english'))

### TOKENIZING ###
def rem(Li:list):
	''' Splits the input if its an alphanum, and removes all the extra symbols, returns a list
        Complexity: O(N) since it there is only one loop, and splitting the string and checking if its alphanum
	'''
	pat ="[a-zA-Z0-9']+"
	return re.findall(pat,Li)

def make_dict(L:list):
    ''' Makes a dictionary with a key of the word and value of the number of occurrences
		returns the dictionary
        Complexity: O(N) since it there is only one loop looping through the list
	'''
    d = {}
    for word in L:
        if word not in stop_words:
            if word not in d:
                d[word]=1
            else:
                d[word]+=1
    return d

def term_freq(total_string):
    token_list = rem(total_string)
    t_freq = make_dict(token_list)
    return t_freq
    
### --------- ###

def create_index(tf, folder, invert_ind):
    for term in tf:
        if term in invert_ind:
            invert_ind[term].append({"freq":tf[term], "docID":folder})
            #print("appended", term, folder)
        else:
            invert_ind[term] = [{"freq":tf[term], "docID":folder}]
            #print("added", term, folder)
        

def html_parse():
    file_path = os.path.join('.', 'WEBPAGES_RAW', 'bookkeeping.json')
    webpage_dict = json.load(open(file_path))
    '''JSON Format   "0/0" : "www.uci.edu" ''' 

    corpus_all = corpus.Corpus()
    '''for m in corpus_all.url_file_map:
        print(m)'''
    
    '''docs is a list of set of words in each doc'''
    docs = list()
    '''dictionary intialization'''

    # FORMAT: { term: [ {freq: #, docID: #}, ...]}
    # Should add - metadata: type (ex: h1, h2, h3, p)

    invert_ind = dict([])

    i = 0
    for folder in webpage_dict:
        address = folder.split("/")
        dir = address[0] # Strings
        file = address[1] # Strings
        
        file_name = os.path.join(".", "WEBPAGES_RAW", dir, file)

        print("FILE:", file_name, "|", file, "|", dir)

        i += 1
        if i > 12:
            break
        if file_name != None:
            with open(file_name, "r", encoding="utf8") as html_doc:
                soup = BeautifulSoup(html_doc, "lxml")
                paragraphs = soup.find_all('p')
                total_string = ""
                for p in paragraphs:
                    total_string += p.text
                tf = term_freq(total_string)
                create_index(tf, folder,invert_ind)
                #for x,y in invert_ind:
                #print(x,"\t",y)

    for term, l in invert_ind.items():
        print(term, ":", l)
                

"""write main function"""
if __name__ == '__main__':
    sys.stdout = open("output2.txt", "w")  # OUTPUT to file called output.txt
    html_parse()
