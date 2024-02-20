from class_document import Document
import pandas as pd

'''Open the files and read their contents.'''

file_1 = open(r'C:/Users/User/Desktop/Search Engine/1txt.txt')
file_2 = open(r'C:/Users/User/Desktop/Search Engine/2txt.txt')
file_3 = open(r'C:/Users/User/Desktop/Search Engine/3txt.txt')

txt1 = Document('txt1', file_1)
txt2 = Document('txt2', file_2)
txt3 = Document('txt3', file_3)

file_1.close()
file_2.close()
file_3.close()

'''Initialize a list of all the documents, which can be extended later. Assign each document a doc id. '''

documents_list = [txt1, txt2, txt3]
doc_id_mapping = {doc: doc_id for doc_id, doc in enumerate(documents_list, 0)}
# print(documents_list)

'''Build a vocabulary of all the terms. '''

terms_list = txt1.terms + txt2.terms + txt3.terms
vocabulary = sorted(set(terms_list))
# print(vocabulary)

'''Build an inverted index.'''

inverted_index = {term: len(documents_list) * [0] for term in vocabulary}   # This needs to be turned into a class
for doc in doc_id_mapping.keys():
    i = doc_id_mapping[doc]   # Returns the doc id
    for term in inverted_index:
        if term in doc.terms:
            inverted_index[term][i] += 1

df = pd.DataFrame.from_dict(inverted_index, orient='index')
df.columns = ['txt1', 'txt2', 'txt3']

print(df)







