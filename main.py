from models.PreProcessing import PreProcessing
from models.Translation import Translation
from enums.enums import Translate

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

def main():
    try:
        # translator = Translation(lang_translation=Translate.EN_TO_PT) 
        # translated_texts = translator.translate_texts(["Hello, world!"]) 
        # print(translated_texts)
        preprocessor = PreProcessing(qchat_en)
    except Exception as e:
        print(f'Deu ruim: \n{e}\n\n')

if __name__ == "__main__":
    main()
