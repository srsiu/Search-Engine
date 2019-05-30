import corpus
import lxml.html
import lxml.etree
import json
import os
import re
from collections import defaultdict
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def rem(Li:list)->str:
	'''splits the input if its an alphanum, and removes all the extra symbols, returns a list
	'''
	'''Complexity: O(N) since it there is only one loop, and splitting the string and checking if its alphanum'''
	pat ="[a-zA-Z0-9']+"
	L = re.findall(pat,Li)
	return L
def make_dict(L:list)-> dict:
	'''makes a dictionary with a key of the word and value of the number of occurrences
		returns the dictionary
	'''
	'''Complexity: O(N) since it there is only one loop looping through the list'''
	d={}
	for word in L:
		if word not in d:
			d[word]=1
		else:
			d[word]+=1	
	return d
def term_freq(total_string):
    token_list = rem(total_string)
    t_freq = make_dict(token_list)
    return t_freq
    
def create_index(tf, folder, invert_ind):
    for term in tf:
        print(type(term))
        invert_ind["Slide"] =5
        if term in invert_ind:
            invert_ind[term].append({"freq":tf[term], "docID":folder})
        else:
            invert_ind[term] = [{"freq":tf[term], "docID":folder}]
        
        

def html_parse():
    file_path = os.path.join('.', 'WEBPAGES_RAW', 'bookkeeping.json')
    webpage_dict = json.load(open(file_path))
    '''JSON Format   "0/0" : "www.uci.edu" ''' 

    corpus_all = corpus.Corpus()
    '''for m in corpus_all.url_file_map:
        print(m)'''
    
    '''docs is a list of set of words in each doc'''
    docs = list()
    '''i think its dictionary intialization'''
    invert_ind = defaultdict(list)
    for folder in webpage_dict:
        address = folder.split("/")
        dir = address[0]
        file = address[1]
        file_name = os.path.join(".", "WEBPAGES_RAW", dir, file)
        
        if file_name != None:
            with open(file_name, "r") as html_doc:
                soup = BeautifulSoup(html_doc, "lxml")
                paragraphs = soup.find_all('p')
                total_string = ""
                for p in paragraphs:
                    total_string += p.text
                tf = term_freq(total_string)
                print(tf)
                invert_ind = create_index(tf, folder,invert_ind)
                #for x,y in invert_ind:
                #print(x,"\t",y)
                
                
                    
"""write main function"""
if __name__ == '__main__':
    html_parse()
                
            
            
        

    

    
        
