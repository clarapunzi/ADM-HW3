# Function used in collector.py to download the webpages

def download_page(url):
    req = urllib.request.urlopen(url)
    webpage = str(req.read())
    with open("article_%d.html" %i, "w") as file:
        file.write(webpage)
    