import corpus
import lxml.html
import lxml.etree
import json
import os
from collections import defaultdict
from bs4 import BeautifulSoup


def html_parse():
    file_path = os.path.join('.', 'WEBPAGES_RAW', 'bookkeeping.json')
    with open(file_path, 'r') as json_file:
        webpage_dict = json.load(json_file)
    '''JSON Format   "0/0" : "www.uci.edu" '''

    corpus_all = corpus.Corpus()
        
    '''docs is a list of set of words in each doc'''
    docs = list()
    for folder in webpage_dict:
        words = set()
        '''print(folder, webpage_dict[folder])'''
        file_name = corpus_all.get_file_name(webpage_dict[folder])
        print(file_name)
        if file_name != None:
            with open(file_name, "r") as html_doc:
                soup = BeautifulSoup(html_doc, "lxml")
                paragraphs = soup.find_all('p')
                for p in paragraphs:
                    print(p.text)
                
                    
"""write main function"""
if __name__ == '__main__':
    html_parse()
                
            
            
        

    

    
        
