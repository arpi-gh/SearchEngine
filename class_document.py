from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\b\w+\b|\$[0-9.]+')


class Document:
    def __init__(self, name, file):
        self.__name = name
        self.__file = file
        self.__terms = tokenizer.tokenize(file.read().lower())

    @property
    def name(self):
        return self.__name

    @property
    def terms(self):
        return self.__terms

    def __repr__(self):
        return self.__name
