from index_utils import idf, tfidf, data_freq, get_key
import json
import math
import re
from itertools import count, combinations
import numpy as np 
import matplotlib.pyplot as plt
import networkx as nx

voc = json.load(open('vocabulary.json'))
actors_dict = json.load(open('actors_dict.json'))
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


# Function that takes a set of document_id in input (integers) and returns a dictionary in which each of them is associated to its years of release

def year_docs(set_docs):
    years = {}
    for i in set_docs:
        file = open('webpages/tsv clean/filtered_%d.tsv' %i).read().split('\n\n')[1].split('\t')
        y = file[9]
        if len(y) == 4:
            years[i] = y
        else:
            res = re.search(r'\d{4}', y)
            if res != None:
                years[i] = res.group(0)
            else: 
                years[i] = 'NA'
    return years 


# Function that takes in input a dictonary of the type: {document_id: released_year} and returns another dict with same keys but the similiarity based on the year of release as values

def sim_docs(years, year_user):
    N = max(abs(int(values)-year_user) for values in years.values())
    sim_years = {}
    for key, values in years.items():
        if values != 'NA':
            sim_years[key] = 1-abs(int(values)-year_user)/N
        else:
            sim_years[key] = 0
    return sim_years


# Function that creates a dictonary in which each actor is associated to the movies in which he played. It doesn't return anything because it save the resulting dictionary in a json file

def actor_dict():
    actors_dict = dict()
    for i in range(10000):
        file = open('webpages/tsv/output_%d.tsv' %i, encoding = 'utf-8').read().split('\n\n')[1].split('\t')
        actors = file[7].split(', ')
        for act in actors:
            if act != '\\n' and act != 'NA' and act!= 'See below' and act != ' ':
                if act not in actors_dict.keys():
                    actors_dict[act] = [i]
                else:
                    actors_dict[act] += [i]
    with open('actors_dict.json', 'w') as a:
        json.dump(actors_dict, a)
        
# Add the nodes to the graph

def add_nodes(list_id):
    G = nx.Graph()
    for i in list_id:
        file = open('webpages/tsv/output_%d.tsv' %i).read().split('\n\n')[1].split('\t')
        actors = file[7].split(', ')
        for act in actors:
            if act != '\\n':
                G.add_node(act.strip()) 
    return G

# Add the edges to the graph

def add_edges(G):
    comb = combinations(G.nodes, 2)
    for couple in list(comb):
        co_star = len(set(actors_dict[couple[0]]).intersection(actors_dict[couple[1]]))
        if co_star >= 2:
            G.add_edge(couple[0],couple[1], weight = co_star)
    return G

# Draw the network

def draw_graph(G):
    network = plt.figure(figsize=(15,8))
    pos = nx.circular_layout(G)

    degrees = G.degree() #Dict with Node ID, Degree
    nodes = G.nodes()
    n_color = np.asarray([degrees[n] for n in nodes])

    #shifted_pos = {k:[v[0],v[1]+.04] for k,v in pos.iteritems()}
    #node_label_handles = nx.draw_networkx_labels(G, pos=shifted_pos, labels=set(nodes))
    d = dict(G.degree)
    elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 4]
    esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <= 4]
    nc = nx.draw_networkx_nodes(G, pos, node_size= [v * 100 for v in d.values()], node_color=n_color, cmap=plt.cm.jet, with_labels = True)
    nx.draw_networkx_edges(G, pos, edgelist=elarge, edge_color='r', width = 5)
    nx.draw_networkx_edges(G, pos, edgelist=esmall, edge_color='g', style='dashed')
    plt.colorbar(nc).set_label('Number of movies in which the actor played')
    return network
