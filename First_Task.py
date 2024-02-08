import re


class NotFoundError(Exception):
    def __init__(self, message='Not found'):
        self.message = message
        super().__init__(self.message)


class Tokenizer:
    token_index = {}

    def tokenize(self, file_path: str) -> None:
        path_pattern = r'.+\.txt$'
        regex = re.compile(path_pattern)
        file_name_match = re.search(r'([^/\\]+(?=\.\w+$))', file_path)
        if file_name_match:
            file_name = file_name_match.group(1)
        else:
            raise ValueError('File name not found')
        if not regex.match(file_path):
            raise ValueError('Invalid file_path')
        with open(file_path) as file:
            contents = file.read()
        contents = re.sub(r'[^\w\s]', '', contents)
        contents = contents.lower()
        tokens = set(contents.split())
        for token in tokens:
            if token not in self.token_index:
                self.token_index[token] = []
            self.token_index[token].append(file_name)


class SearchEngine:
    def search(self, keyword: str, database: Tokenizer) -> str:
        if keyword in database.token_index:
            return database.token_index[keyword]
        else:
            print('NotFound')


if __name__ == '__main__':
    with open(r'C:/Users/User/Desktop/Search Engine/1txt.txt', 'w') as txt1:
        txt1.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                   'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris '
                   'nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate '
                   'velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non '
                   'proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')

    with open(r'C:/Users/User/Desktop/Search Engine/2txt.txt', 'w') as txt2:
        txt2.write('Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, '
                   'totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae '
                   'dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, '
                   'sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro '
                   'quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non '
                   'numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim '
                   'ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid '
                   'ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse '
                   'quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?')

    with open(r'C:/Users/User/Desktop/Search Engine/3txt.txt', 'w') as txt3:
        txt3.write('But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was '
                   'born and I will give you a complete account of the system, and expound the actual teachings of '
                   'the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, '
                   'or avoids pleasure itself, because it is pleasure, but because those who do not know how to '
                   'pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there '
                   'anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because '
                   'occasionally circumstances occur in which toil and pain can procure him some great pleasure. To '
                   'take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain '
                   'some advantage from it? But who has any right to find fault with a man who chooses to enjoy a '
                   'pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant '
                   'pleasure?')

    tk = Tokenizer()
    tk.tokenize(r'C:/Users/User/Desktop/Search Engine/1txt.txt')
    tk.tokenize(r'C:/Users/User/Desktop/Search Engine/2txt.txt')
    tk.tokenize(r'C:/Users/User/Desktop/Search Engine/3txt.txt')
    data = tk.token_index
    for key, values in data.items():
        print(f"{key}: {values}")

    search_engine = SearchEngine()
    keyword = None
    while keyword != 'EXIT':
        keyword = str(input('Search: \n'))
        print(search_engine.search(keyword, tk))


