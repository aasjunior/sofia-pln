from enum import Enum

class Language(Enum):
    PT = 'portuguese'
    EN = 'english'
 
class LanguageModel(Enum):
    PT_BR = 'pt_core_news_lg'
    EN = 'en_core_web_trf'

class Translate(Enum):
    EN_TO_PT = 'translation_en_to_pt'
    PT_TO_EN = 'translation_pt_to_en'