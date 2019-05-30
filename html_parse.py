import corpus
import lxml.html
import lxml.etree
import json
import os
from collections import defaultdict
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def html_parse():
    file_path = os.path.join('.', 'WEBPAGES_RAW', 'bookkeeping.json')
    webpage_dict = json.load(open(file_path))
    '''JSON Format   "0/0" : "www.uci.edu" ''' 

    corpus_all = corpus.Corpus()
    '''for m in corpus_all.url_file_map:
        print(m)'''
    
    '''docs is a list of set of words in each doc'''
    docs = list()
    for folder in webpage_dict:
        address = folder.split("/")
        dir = address[0]
        file = address[1]
        file_name = os.path.join(".", "WEBPAGES_RAW", dir, file)
        
        if file_name != None:
            with open(file_name, "r") as html_doc:
                soup = BeautifulSoup(html_doc, "lxml")
                paragraphs = soup.find_all('p')
                for p in paragraphs:
                    print(p.text)
                
                    
"""write main function"""
if __name__ == '__main__':
    html_parse()
                
            
            
        

    

    
        
