import pandas as pd
import nltk

qchat_en = [
    'Does the child look at you when you call their name?',
    'Can you make eye contact with the child?',
    'Does the child point to indicate that they want something? (e.g.: a toy that is out of reach)',
    'Does the child point to share something that catches their attention? (e.g.: pointing at an interesting scenery)',
    'Does the child "pretend"? (e.g.: taking care of dolls, talking on a toy phone)',
    'Does the child follow your gaze?',
    'If you or someone in your family is visibly upset, does the child show signs of wanting to comfort them? (e.g.: stroking hair, hugging)',
    'Has the child started speaking?',
    'Does the child use simple gestures? (e.g.: waving goodbye)',
    'Does the child stare at nothing for no apparent reason?'
]

class PreProcessing:
    def __init__(self, texts: list, language: str = 'english'):
        self.texts = texts
        self.tokenized = list()
        self.num_tokens = 0
        self.types = None
        self.normalized = list()
        self.radicalized = list()
        self.pos_tagged = list()
        self.chunks = list()
        self.stopwords = nltk.corpus.stopwords.words(language)
        self.snowballStemmer = nltk.SnowballStemmer(language)
        self._initialize()

    def _tokenize(self):
        self.tokenized = [nltk.word_tokenize(text) for text in self.texts]
        self.types = set(word.lower() for tokens in self.tokenized for word in tokens)
        self.num_tokens = sum(len(token_list) for token_list in self.tokenized)

    def _normalize(self):
        self.normalized = [[word.lower() for word in words if word not in self.stopwords] for words in self.tokenized]

    def _radicalize(self):
        self.radicalized = [[self.snowballStemmer.stem(word) for word in words] for words in self.normalized]

    def _pos_tagging(self):
        self.pos_tagged = [nltk.pos_tag(word) for word in self.radicalized]

    def _chunking(self):
        self.chunks = [nltk.ne_chunk(tagged) for tagged in self.pos_tagged]

    def info(self):
        print(f'Quantidade de registros: \n{len(self.texts)}\n\n')
        print(f'Tokenização: \n{self.tokenized}\n\n')
        print(f'Quantidade de tokens: \n{self.num_tokens}\n\n')
        print(f'Quantidade de types (tipos únicos de tokens): \n{len(self.types)}\n\n')
        print(f'Types: \n{self.types}\n\n')
        print(f'Remoção das stopwords: \n{self.normalized}\n\n')
        print(f'Radicalização: \n{self.radicalized}\n\n')
        print(f'Pos Tagging: \n{self.pos_tagged}\n\n')
        print(f'Análise semântica (Chunking): \n{self.chunks}\n\n')

    def _initialize(self):
        try:
            self._tokenize()
            self._normalize()
            self._radicalize()
            self._pos_tagging()
            self._chunking()

            self.info()
        
        except Exception as e:
            raise RuntimeError(f'Erro na inicialização: \n{e}\n\n')


pln = PreProcessing(qchat_en)
