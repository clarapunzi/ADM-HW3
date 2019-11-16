import pandas as pd
import csv
from bs4 import BeautifulSoup

# Global variables:

head_wiki = ['Directed by', 'Produced by', 'Written by', 'Starring', 'Music by', 'Release date', 'Running time', 'Country', 'Language', 'Budget']
head = ['title', 'intro', 'plot', 'film_name', 'director', 'producer', 'writer', 'starring', 'music', 'release date', 'runtime', 'country', 'language', 'budget']
infos = ['NA']*14

''' # In this step I have also created a dictionary to get the links of the 'disambiguation' pages (around 100). 
After that, I modified the urls of these pages and correct them with new ones.
'''
NOTlinks = {}  

for i in range(10000):
    try:
        page = open('article_%d.html' %i).read()
        soup = BeautifulSoup(page, 'html.parser')
        infos = parse_page(soup)
    
        with open('output_%d.tsv'%i, 'w') as out_file:
            tsv_writer = csv.writer(out_file, delimiter='\t')
            tsv_writer.writerow(head)
            tsv_writer.writerow(infos)
    except:
        page = open('article_%d.html' %i).read()
        soup = BeautifulSoup(page, 'html.parser')
        NOTlinks[i] = soup.title.text[:-12]
