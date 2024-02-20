# Overview
This Python program is a simple implementation of a search engine that uses an inverted index. The latter is a data structure that maps terms (tokens or words) with the documents. In other words, the result is a binary term-document incidence matrix. 

# Features
- A separate **class Document** for documents. Each instance stores the name of the document, as well as its tokenized content. The latter is stored as a list. The name and the terms(words) of the docuement can be accessed from the outside. 
- **Inverted Index** construction. An inverted index is constructed  using Python's built-in dictionary data structure, where the keys are the terms(words) and the values are a vector space representation of the documents the terms appear in. The terms are sorted alphabetically.
- A separate **class SearchEngine** for the search engine. This class has a pulic method called _search_ and a private method called _intersection_. The search returns a list of all the documents containing all of the keywords that the user searched combined.

# Usage
1. Run the program
   python3 main.py

2. Follow the prompt
   - The program will first display the inverted index
   - It will prompt you to enter a search term
   - After you hit ENTER, the program will display a list of all the documents the term appears in in human-readable format (the name of the documents).
    
# Dependencies
- Python3

# File Structure 
  - **class_document.py**: a file containing the Document class, which is imported in main.py. 
  - **Inverted_index.py**: a file containing the implementation of an inverted index. 
  - **Search_Engine.py** : the implementation of the search engine itself. 
  - **main.py**: the main driver program for searching. 
 
