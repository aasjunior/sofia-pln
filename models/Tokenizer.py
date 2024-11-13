from nltk import word_tokenize

class Tokenizer:
    def __init__(self, stopwords=None):
        self.stopwords = stopwords or []

    def tokenize(self, texts: list):
        try:
            tokenized = [word_tokenize(text) for text in texts]
            types = set(word.lower() for tokens in tokenized for word in tokens)
            num_tokens = sum(len(tokens) for tokens in tokenized)

            return tokenized, types, num_tokens
        
        except Exception as e:
            raise RuntimeError(f'Erro na tokenização: \n{e}\n\n')
    
    def remove_stopwords(self, tokenized_texts):
        try:
            return [[word for word in tokens if word.lower() not in self.stopwords] for tokens in tokenized_texts]
        
        except Exception as e:
            raise RuntimeError(f'Erro na remoção das stopwords: \n{e}\n\n')