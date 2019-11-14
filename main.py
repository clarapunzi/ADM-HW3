import utils
from parser_utils import clean_ls
import json
import pandas as pd
import heapq

urls = json.load(open('urls.json'))
voc = json.load(open('vocabulary.json'))
inverted_index = json.load(open('inverted_index.json'))
inverted_index_freq = json.load(open('inverted_index_freq.json'))

# 1° SEARCH ENGINE

def search_engine_1(query_match):
    df = pd.DataFrame(columns=['Title','Intro','Wikipedia Url'])
    for i in query_match:
        file = open('webpages/tsv/output_%d.tsv' %i).read().split('\n\n')[1].split('\t')
        title, intro, link = file[3].encode('utf8').decode("unicode_escape"), file[1].encode('utf8').decode("unicode_escape"), urls[str(i)]
        new_row = {'Title':title, 'Intro': intro, 'Wikipedia Url': link}
        df = df.append(new_row, ignore_index=True)
    
    d = dict(selector="th", props=[('text-align', 'center')])
    df.style.format({'Wikipedia Url': utils.make_clickable}).hide_index().set_table_styles([d]).set_properties(**{'text-align': 'center'}).set_properties(subset=['Title'], **{'width': '130px'})
    return df


# SEARCH ENGINE 2

def search_engine_2(query, query_match):
    #Build the query vector
    query_vec = utils.query_vector(query)

    # Build the heap structure
    sim_dict = {}
    for i in query_match:
        sim_dict[i] = utils.cosine_similarity(query_vec, i)

    df = pd.DataFrame(columns=['Title','Intro','Wikipedia Url', 'Similarity'])

    for sim in heapq.nlargest(5, sim_dict.items(), key = lambda i: i[1]):
        i = sim[0]  # document_id
        file = open('webpages/tsv/output_%d.tsv' %i).read().split('\n\n')[1].split('\t')
        title, intro, link = file[3].encode('utf8').decode("unicode_escape"), file[1].encode('utf8').decode("unicode_escape"), urls[str(i)]
        new_row = {'Title':title, 'Intro': intro, 'Wikipedia Url': link, 'Similarity': sim[1]}
        df = df.append(new_row, ignore_index=True)

    # Visualization of the top 5 documents related to the query
    d = dict(selector="th", props=[('text-align', 'center')])
    df1 = df.sort_values(by=['Similarity'], ascending = False)
    df1.style.format({'Wikipedia Url': utils.make_clickable}).hide_index().set_table_styles([d]).set_properties(**{'text-align': 'center'}).set_properties(subset=['Title'], **{'width': '130px'})
    return df

# SEARCH ENGINE 3

# Once the documents that match the query have been selected, we rank them by our new definition of similarity which considers more similar movies whose years of release are closer

def search_engine_3(query_match):
    print('In which year was the movie released?')
    year_user = int(input())

    # Rank the results by closeness to a given year
    years = utils.year_docs(query_match)
    sim_years = utils.sim_docs(years, year_user)

    df = pd.DataFrame(columns=['Title','Intro','Wikipedia Url', 'Similarity'])

    for sim in heapq.nlargest(5, sim_years.items(), key = lambda i: i[1]):
        i = sim[0]  # document_id
        file = open('webpages/tsv/output_%d.tsv' %i).read().split('\n\n')[1].split('\t')
        title, intro, link = file[3].encode('utf8').decode("unicode_escape"), file[1].encode('utf8').decode("unicode_escape"), urls[str(i)]
        new_row = {'Title':title, 'Intro': intro, 'Wikipedia Url': link, 'Similarity': sim[1]}
        df = df.append(new_row, ignore_index=True)

    # Visualization of the top 5 documents related to the query
    d = dict(selector="th", props=[('text-align', 'center')])
    df1 = df.sort_values(by=['Similarity'], ascending = False)
    df1.style.format({'Wikipedia Url': utils.make_clickable}).hide_index().set_table_styles([d]).set_properties(**{'text-align': 'center'}).set_properties(subset=['Title'], **{'width': '130px'})
    return df

# Ask the user to input a query
print('What do you want to search?')
query = input().split()  

# Clean the query with the auxiliary function clean_ls in parser_utils.py
query = clean_ls(query)

# Get the term_id of the words in the query (integers)
query_index = [voc[word] for word in query]

# Get the document_if of the documents containing the words in the query
allDOC = [inverted_index[str(word)] for word in query_index]
query_match = set(allDOC[0]).intersection(*allDOC[1:])

# Ask the user to choose a search engine
print('What kind of query search do you want to execute?', 
      '  -> Enter 1 if you want to see the result of a simple conjunctive query search',
     '  -> Enter 2 if you want to see the top 3 results of a conjunctive query search based on text similarity',
     '  -> Enter 3 if you want to perform an advanced query search', sep ='\n')
search_engine = int(input())

if search_engine == 1:
    qs1 = search_engine_1(query_match)
    print(qs1)
elif search_engine == 2:
    qs2 = search_engine_2(query, query_match)
    print(qs2)
elif search_engine == 3:
    qs3 = search_engine_3(query_match)
    print(qs3)
else:
    print('Incorrect input')

