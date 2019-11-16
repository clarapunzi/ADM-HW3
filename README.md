### ADM-HW3

Lot of file of this project use the same librarys. In particular we import: *json* for: **main.py**, **collector.py**, **index.py**, **utils.py**.
The library *csv* for **collector.py** and **parser.py**, *pandas* for **main.py**,  **collector.py**, **index.py** and **parser.py**.

Also in **collector.py** are used:
* HTMLParser
* time
* urllib.request

in **utils.py**:
* math
* url
* count and combination from itertools
* numpy
* matplotlib.pyplot
* networkx
in **main.py**:
* heapq
* clean_ls form parser_utils

and in **parser.py** we use the BeautifulSoup from bs4.


#### main.py ####
With this file we can choose the tipology of search that we want to do.
In particular we have 3 option, the first is the semple search the second is with the similarity and the third is our solution, such as with the year of production of the film.
In this file we have 3 function: _search_engine_1_, _search_engine_2_, _search_engine_3_.

The first return only the Title, Intro and the Url of the pages.
The second return the Title, Intro, the Url and the Similarity between the different result page.

The third return our score and Similarity, in this specific case we use the year how new reference for the score.


#### collector.py ####

We created this file with the  _handle_starttag_ function to parse the HTML pages, in this way it is possible to take all the URL that there are in the HTML file.

In the for loop we call the function _download_page_. With this function is possible to download the HTML pages from the URL that we had before download.
_download_page_ function is present in *collector_utils.py*  file.

#### collector_utils.py ####
In this file we wrote the  _download_page_ function.
This function take in input the URL of the page that we want download and in output return the HTML pages.

#### parser.py ####

In this file we call the function _parse_page_ thet you can find in the *parser_utils.py* file.
There are the global variables that we use to devide and take the information.
In this way we can open the HTML pages, parse the file with the global variable and at the end return in output a .tsv file.

#### parser_utils.py #### 
In this file there is the main parser function, such as _parse_page_. With this function is possible to find all the table tag that there are in an HTML file, after that it is possible to take all the information about the page using the global variables.

#### index.py ####
In this file you can find the two main part on the first two type of research.
Also we create a vocabolary that we use to compare the different vocabolary, in this way is possible to have a good index for the file.

#### index_utils.py ####
In this file there are four function:
* _data_freq_
  - in this function we count how many times one word appears in the same file;
* _idf_
  - With this function we calculate the inverse data frequency of a word that is in the vocabulary;
* _tfidf_
  - With this function we calculate the term frequency. It is calculate with the _idf_ funcion;
* _get_key_
  - This function return the term that is link at the term_id that the user insert in input.

#### utils.py ####

In this file there are all the functions that we use for different file.
Also that there are the functions _add_node_, _add_edges_ and _drow_graph_ that you can use for the bonus Step.
In particularrly in this file there are:
* _query_vector_ create the vector of a query;
* _vector_ that create the vectors of a determined file;
* _cosine_similarity_  return the cosine similarity between two vector. In particular the cosine similarity is the mesure of similarity between two vectors that mesure the cosine angele between them.
* _make_clickable_ that permit a value to became clickable.
* _year_docs_ is the function that we use to solved the third point of the homework. With this function is possible to take the production's year of the movie.
* _sim_docs_ is a function that takes in input a dictonary and returns a new dictionary with the same keys but the similiarity that based on the year of release as values.     
* _actor_dic_  creates a dictonary in which each actor is associated to the movies in which he played.

#### excercise_4.py ####
In this file there is the function that permit to solve the excercise and to find the subsequence of a word.
May be this solution is not the best.

#### main.ipynb ####
In this Jupyter file there are all the strategies that we had adopt to solve all the point of this homework.
    
