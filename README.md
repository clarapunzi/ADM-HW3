### ADM-HW3

Many files of this project use common libraries. In particular we import: *json* in **main.py**, **collector.py**, **index.py**, **utils.py**, the library *csv* in **collector.py** and **parser.py**, *pandas* in **main.py**,  **collector.py**, **index.py** and **parser.py**.

Also in **collector.py** are used:
* HTMLParser
* time
* urllib.request.

In **utils.py**:
* math
* url
* count and combination from itertools
* numpy
* matplotlib.pyplot
* networkx.

In **main.py**:
* heapq

and in **parser.py** we use the BeautifulSoup from bs4.


#### main.py ####
With this file we can choose the tipology of search that we want to do.
In particular we have 3 options corresponding to three different functions:  _search_engine_1_, _search_engine_2_, _search_engine_3_.
The first is the simple search and returns only the Title, Intro and the Url of the pages.

The second takes into account the cosine similarity and uses this as a ranking parameter among the different documents that match the query.

The third is our solution, i.e. with similarity based on the year of production of the film; it returns again Title, Intro and the Url of the pages ranked by this new similarity.

#### collector.py ####

We created this file with the  _handle_starttag_ function to parse the HTML pages, in this way it is possible to extract all the URLs that there are in the HTML file.

In the for loop we call the function _download_page_. With this function is possible to download the HTML pages from the URL that we had before download.
_download_page_ function is stored in the file *collector_utils.py*.

#### collector_utils.py ####
In this file we wrote the  _download_page_ function.
This function takes in input the URL of the page that we want download and in output returns the HTML pages.

#### parser.py ####
In this file we call the function _parse_page_ thet you can find in the *parser_utils.py* file.
There are the global variables that we use to devide and take the information.
In this way we can open the HTML pages, parse the file with the global variable and at the end return in output a .tsv file.

#### parser_utils.py #### 
In this file there is the main parser function, that is, _parse_page_. With this function it is possible to find all the <table> and <p> tags that there are in an HTML file and after that it is possible to organise and store the information about the movie using the global variables.

#### index.py ####
In this file you can find the code to generate the indexes for the first two types of research.
Also we create a vocabolary that associates each possible word in our documents to an integer identifier.

#### index_utils.py ####
In this file there are four function:
* _data_freq_
  - this function evaluate the frequency of a word in a specific file;
* _idf_
  - With this function we calculate the inverse data frequency of a word with respect to the whole set of documents;
* _tfidf_
  - With this function we calculate the term frequency - inverse data frequency of a word in a given document. It is calculated by multiplying the results of the previous two functions;
* _get_key_
  - This function return the term that is linked to the term_id that the user insert in input.

#### utils.py ####

In this file there are all the functions that we use for different file.
Also that there are the functions _add_node_, _add_edges_ and _drow_graph_ that you can use for the bonus Step.
In particular in this file there are:
* _query_vector_ creates the vector of a query;
* _vector_ that create the vectors of a given file;
* _cosine_similarity_  return the cosine similarity between two vectors; specifically, it is given by the cosine angle between them.
* _make_clickable_ that permit a value to became clickable.
* _year_docs_ is the first function we used to solve the third point of the homework; it extracts the year of release of a movie from the *.tsv* files.
* _sim_docs_ is a function that takes in input a dictonary and returns a new dictionary with the same keys but the similiarity based on the year of release as values.     
* _actors_dic_  creates a dictonary in which each actor is associated to the movies in which he played.

#### excercise_4.py ####
In this file there is the function that permit to solve the excercise and to find the subsequence of a word.
Maybe this solution is not optimal.

#### main.ipynb ####
In this Jupyter file there are all the strategies that we had adopted to solve all the point of this homework.
    
