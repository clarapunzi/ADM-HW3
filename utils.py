# The following functions are necessary to execute the query search in part 2.2

# Build the query vector

def query_vector(query):
    query_vector = {}
    for word in query:  # words are strings
        df = query.count(word)/len(query)
        query_vector[voc[word]] = df * idf(word)
    return query_vector

# Function that returns the vector of a certain document

def vector(i):  # integer
    vec = {}
    file = open('webpages/tsv clean/filtered_%d.tsv'%i).read().split('\n\n')[1]
    tabs = file.split('\t')[1]+file.split('\t')[2]  # list of words in intro and plots
    for word in tabs.split():
        vec[voc[word]] = tfidf(voc[word], i)
    return vec

# Function that returns the cosine similarity of two given vectors (usually, the query vector and the vector represnting a document)

def cosine_similarity(query_vec, document_id):  # (dict, integer)
    norm_query = math.sqrt(sum(n**2 for n in query_vec.values()))
    norm_doc = math.sqrt(sum(tfidf(word,document_id) for word in vector(document_id)))
    dot_pr = 0
    for word in query_vec.keys():
        dot_pr += query_vec[word]*tfidf(word, document_id)  # (string, integer)
    return dot_pr/(norm_query*norm_doc)

# Function that make the links clickable when printing the output of a query search

def make_clickable(val):  
    return '<a target="_blank" href="{}">{}</a>'.format(val, val)
