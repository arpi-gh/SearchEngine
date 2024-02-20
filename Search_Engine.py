from Inverted_index import inverted_index
from Inverted_index import doc_id_mapping


class SearchEngine:

    @staticmethod
    def __intersection(keyword_vectors: list):
        result = len(keyword_vectors[0]) * [1]
        for j in range(len(keyword_vectors)):
            for i in range(len(keyword_vectors[0])):
                result[i] = result[i] & keyword_vectors[j][i]
        return result

    def search(self, database: dict, keywords: list):
        result = []
        vector_space = []
        for keyword in keywords:
            if keyword in database.keys():
                vector_space.append(database[keyword])
        result_vector = self.__intersection(vector_space)
        for res in range(len(result_vector)):
            if result_vector[res] == 1:
                for doc in doc_id_mapping:
                    if doc_id_mapping[doc] == res:
                        result.append(doc)
        return result



