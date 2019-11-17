import json
voc = json.load(open('vocabulary.json'))
inverted_index = json.load(open('inverted_index.json'))
import math
N = 30000

# Function that returns the data frequency (integer) of a term (string) in a specified document (i)

def data_freq(term, i):
    file = open('webpages/tsv clean/filtered_%d.tsv'%i).read().split('\n\n')[1]
    tabs = file.split('\t')[1]+file.split('\t')[2]  # list of words in intro and plots
    if term in tabs.split():
        df = tabs.split().count(word)/len(tabs.split())
    else:
        df = 0
    return df


# Function that returns the inverse data frequency of a word in the vocabulary 

def idf(term):
    val = len(inverted_index[str(voc[word])])  # this is the number of documents containing the given word
    return math.log(N/val)


# Function that returns the term frequency - inverse document frequency 

def tfidf(term_id, document_id): # (integer, integer)
    return data_freq(get_key(term_id), document_id)*idf(get_key(term_id))


# Function that returns the a term given its term_id

def get_key(term_id): 
    for key, value in voc.items(): 
         if term_id == value:
                return key   
    return "key doesn't exist"
