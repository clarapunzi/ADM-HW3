from html.parser import HTMLParser
import pandas as pd
import json 
import csv
import time     #For Delay
import urllib.request    #Extracting web pages
from collector_utils import download_page

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag != 'a':
            return
        self.urls.append(attrs[0][1])

page = open('movies1.html').read()
parser = MyHTMLParser()
parser.urls = []
parser.feed(page)

    
# Download the webpages
    
for i in index:
    try:
        download_page(parser.urls[i])
        time.sleep(1)
    except:
        time.sleep(1200)

        
# Save an indexed list of the urls in a json file

d = {}
for n, url in enumerate(parser.urls):
    d[n]=url

with open('urls.json', 'w') as fp:
    json.dump(d, fp)
