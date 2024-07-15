from projeto.persistence.mongodb.paragraph_repository_impl import ParagraphRepository

from deep_translator import GoogleTranslator

class TranslationService:
    def __init__(self, mongo_config):
        self.mongo_config = mongo_config

    def translate_paragraph(self, text, source_lang, target_lang):
        try:
            translator = GoogleTranslator(source=source_lang, target=target_lang)
            translated_text = translator.translate(text)
            return translated_text
        except Exception as e:
            print(f"Translation error: {e}")
            return None
