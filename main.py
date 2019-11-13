import pandas as pd
import json 

urls = json.load(open('urls.json'))
voc = json.load(open('vocabulary.json'))
inverted_index = json.load(open('inverted_index.json'))


# Ask the user to input a query
query = input().split()  

# Clean the query with the auxiliary function clean_ls in parser_utils.py
query = clean_ls(query)

# Get the term_id of the words in the query (integers)
query_index = [voc[word] for word in query]

# Get the document_if of the documents containing the words in the query

allDOC = [inverted_index[str(word)] for word in query_index]
query_match = set(allDOC[0]).intersection(*allDOC[1:])


# 1° SEARCH ENGINE

# Show the result of the query in a dataframe
df = pd.DataFrame(columns=['Title','Intro','Wikipedia Url'])

for film in query_match:
    i = int(film)
    file = open('C:/Users/Clara/Desktop/sapienza/ADM/HM3/webpages/tsv/output_%d.tsv' %i).read().split('\n\n')[1].split('\t')
    title, intro, link = file[3].encode('utf8').decode("unicode_escape"), file[1].encode('utf8').decode("unicode_escape"), urls[str(film)]
    new_row = {'Title':title, 'Intro': intro, 'Wikipedia Url': link}
    df = df.append(new_row, ignore_index=True)
    
d = dict(selector="th", props=[('text-align', 'center')])
df.style.format({'Wikipedia Url': make_clickable}).hide_index().set_table_styles([d]).set_properties(**{'text-align': 'center'}).set_properties(subset=['Title'], **{'width': '130px'})



# SEARCH ENGINE 2

#Build the query vector
query_vec = query_vector(query)

# Build the heap structure
sim_dict = {}
for i in query_match:
    sim_dict[i] = cosine_similarity(query_vec, i)

# Show the result of the query in a dataframe
df = pd.DataFrame(columns=['Title','Intro','Wikipedia Url', 'Similarity'])

for sim in heapq.nlargest(3, sim_dict.items(), key = lambda i: i[1]):
    i = sim[0]  # document_id
    file = open('webpages/tsv/output_%d.tsv' %i).read().split('\n\n')[1].split('\t')
    title, intro, link = file[3].encode('utf8').decode("unicode_escape"), file[1].encode('utf8').decode("unicode_escape"), urls[str(i)]
    new_row = {'Title':title, 'Intro': intro, 'Wikipedia Url': link, 'Similarity': sim[1]}
    df = df.append(new_row, ignore_index=True)

# Visualization of the top 5 documents related to the query

d = dict(selector="th", props=[('text-align', 'center')])
df1 = df.sort_values(by=['Similarity'], ascending = False).head(5)
df1.style.format({'Wikipedia Url': make_clickable}).hide_index().set_table_styles([d]).set_properties(**{'text-align': 'center'}).set_properties(subset=['Title'], **{'width': '130px'})






