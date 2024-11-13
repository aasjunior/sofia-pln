from nltk import SnowballStemmer
from enums.enums import Language

class Stemmer:
    def __init__(self, language: Language = Language.EN):
        self.stemmer = SnowballStemmer(language.value)

    def stem(self, tokens: list):
        try:
            print(tokens)
            return [self.stemmer.stem(token.lower()) for token in tokens]
        
        except Exception as e:
            raise RuntimeError(f'Erro na radicalização: \n{e}\n\n')