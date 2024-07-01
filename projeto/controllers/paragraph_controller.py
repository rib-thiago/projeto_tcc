from projeto.services.translation_service import TranslationService

class ParagraphController:
    def __init__(self):
        self.translation_service = TranslationService()

    def translate_paragraph(self, paragraph_id, translation_data):
        """ Realiza a tradução de um parágrafo """
        return self.translation_service.translate_paragraph(paragraph_id, translation_data)

    def list_paragraphs_to_translate(self, document_id):
        """ Lista os parágrafos de um documento que ainda não foram traduzidos """
        return self.translation_service.list_paragraphs_to_translate(document_id)
