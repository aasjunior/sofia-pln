from transformers import MBartForConditionalGeneration, MBart50Tokenizer
from enums.enums import Translate

class Translation:
    def __init__(self, lang_translation: Translate):
        self.model_name = "facebook/mbart-large-50-many-to-many-mmt"
        self.model = MBartForConditionalGeneration.from_pretrained(self.model_name)
        self.tokenizer = MBart50Tokenizer.from_pretrained(self.model_name)
        self.src_lang = "en_XX" if lang_translation == Translate.EN_TO_PT else "pt_XX"
        self.tgt_lang = "pt_XX" if lang_translation == Translate.EN_TO_PT else "en_XX"

    def translate_texts(self, texts: list):
        try:
            translated_texts = []
            for text in texts:
                inputs = self.tokenizer(text, return_tensors="pt", padding=True)
                translated_tokens = self.model.generate(**inputs, forced_bos_token_id=self.tokenizer.lang_code_to_id[self.tgt_lang])
                translated_text = self.tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]
                translated_texts.append(translated_text)
            return translated_texts
        
        except Exception as e:
            raise RuntimeError(f'Erro na tradução: \n{e}\n\n')

