from enums.enums import Language
import spacy

class Lemmatizer:
    def __init__(self, language: Language):
        self.language = language
        self.nlp = spacy.load('pt_core_news_lg' if language == Language.PT else 'en_core_web_trf')

    def process(self, texts: list):
        try:
            """Lematiza os textos fornecidos.""" 
            return [[token.lemma_ for token in self.nlp(text)] for text in texts]
        
        except Exception as e:
            raise RuntimeError(f'Erro na lematização: \n{e}\n\n')