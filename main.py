from Search_Engine import SearchEngine
from Inverted_index import inverted_index

if __name__ == '__main__':
    search = SearchEngine()
    keys = input('Search: ').lower().split()
    print(search.search(database=inverted_index, keywords=keys))
