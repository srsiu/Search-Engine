import corpus
import lxml.html
import lxml.etree
import json
import os
from collections import defaultdict


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

        file_name = corpus_all.get_file_name(webpage_dict[folder])
        if file_name != None:
            with open(file_name, "rb") as html_doc:
                tree = lxml.etree.HTML(html_doc)
                etree.tostring(tree)

"""write main function"""
if __name__ == '__main__':
    html_parse()
                
            
            
        

    

    
        
