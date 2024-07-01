from persistence.mongodb.paragraph_repository_impl import ParagraphRepository

class TranslationService:
    def __init__(self):
        self.paragraph_repository = ParagraphRepository()

    def translate_paragraph(self, paragraph_id, translation_data):
        """ Realiza a tradução de um parágrafo """
        return self.paragraph_repository.translate_paragraph(paragraph_id, translation_data)

    def list_paragraphs_to_translate(self, document_id):
        """ Lista os parágrafos de um documento que ainda não foram traduzidos """
        return self.paragraph_repository.list_paragraphs_to_translate(document_id)
