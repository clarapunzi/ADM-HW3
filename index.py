import json
import pandas as pd

# Create the file 'vocabulary.json' in which each term in intro and plot is mapped to an integer (term_id) 

words = set() 
for i in range(10000):
    file = open('webpages/tsv clean/filtered_%d.tsv'%i).read().split('\n\n')[1]
    tabs = file.split('\t')[1]+file.split('\t')[2]  # list of words in intro and plots
    words.update(tabs.split())

voc = dict()
for term_id, term in enumerate(words):
    voc[term]= term_id  
    
with open('vocabulary.json', 'w') as fp:
    json.dump(voc, fp)
    

#  1° SEARCH ENGINE
    
# Create the inverted index and save it to a json file

inverted_index = dict.fromkeys(range(len(voc)), [])
for i in range(10000):
    file = open('webpages/tsv clean/filtered_%d.tsv'%i).read()
    lines = file.split('\n\n')[1]
    tabs = lines.split('\t')[1]+lines.split('\t')[2]  # list of words in intro and plots
    for word in set(tabs.split()):
        inverted_index[voc[word]] = inverted_index[voc[word]]+[i]

with open('inverted_index.json', 'w') as fp:
    json.dump(inverted_index, fp)        
  


# 2° SEARCH ENGINE

# Create the second inverted index, that is of the type:  {term_id : [document_id, TF-IDF_{document_id, term}]] 

inverted_index_freq = dict.fromkeys(range(len(voc)))
for term_id in inverted_index_freq.keys():
    for document_id in inverted_index[str(term_id)]:
        if inverted_index_freq[term_id] == None:
            inverted_index_freq[term_id] = [(document_id, tfidf(term_id, document_id))]
        else:
            inverted_index_freq[term_id] += [(document_id, tfidf(term_id, document_id))]

# The new inverted_index_freq is as follow: {term_id : [document_id, TF-IDF_{document_id, term}]] 
        
with open('inverted_index_freq.json', 'w') as fp:
    json.dump(inverted_index_freq, fp)        
        
        
        
        
        
        
