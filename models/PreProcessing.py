from models.Tokenizer import Tokenizer
from models.Stemmer import Stemmer
from models.Lemmatizer import Lemmatizer
from models.Translation import Translation
from enums.enums import Language, Translate
from nltk.corpus import stopwords

class PreProcessing:
    def __init__(self, texts: list, language: Language = Language.EN):
        self.texts = texts
        self.language = language
        self.tokenizer = Tokenizer(stopwords=self._get_stopwords(language))
        self.stemmer = Stemmer(language=language)
        self.lemmatizer = Lemmatizer(language=language)
        self.translator = Translation(lang_translation=Translate.PT_TO_EN if language == Language.PT else Translate.EN_TO_PT)

        self.tokenized = []
        self.normalized = []
        self.radicalized = []
        self.lemmatized = []
        self.translated = []
        self._initialize()
    
    def _get_stopwords(self, language: Language):
        """Retorna as stopwords de acordo com o idioma selecionado."""
        try:
            return stopwords.words(language.value)

        except Exception as e:
            raise RuntimeError(f'PreProcessing Erro no get_stopwords: \n{e}\n')


    def _tokenize(self):
        """Tokeniza os textos usando a classe Tokenizer."""
        self.tokenized, self.types, self.num_tokens = self.tokenizer.tokenize(self.texts)

    def _normalize(self):
        """Normaliza os textos removendo as stopwords."""
        self.normalized = self.tokenizer.remove_stopwords(self.tokenized)

    def _stem(self):
        """Radicaliza os textos usando a classe Stemmer."""
        self.radicalized = [self.stemmer.stem(sentence) for sentence in self.normalized]

    def _lemmatize(self):
        """Lematiza os textos usando a classe Lemmatizer."""
        self.lemmatized = [self.lemmatizer.process(sentence) for sentence in self.normalized]

    def _translate(self):
        """Traduz os textos usando a classe Translation."""
        self.translated = self.translator.translate_texts(self.texts)

    def info(self):
        """Exibe informações sobre o processamento dos textos."""
        print(f'Tokenized: \n{self.tokenized}\n\n')
        print(f'Normalized: \n{self.normalized}\n\n')
        print(f'Radicalized: \n{self.radicalized}\n\n')
        print(f'Lemmatized: \n{self.lemmatized}\n\n')
        print(f'Translated: \n{self.translated}\n\n')

    def _initialize(self):
        """Inicializa o processo de pré-processamento."""
        try:
            self._tokenize()
            self._normalize()
            self._stem()
            self._lemmatize()
            self._translate()

            self.info()

        except Exception as e:
            raise RuntimeError(f'Erro na inicialização do pré-processamento: \n{e}\n')