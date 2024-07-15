from projeto.persistence.mongodb.paragraph_repository_impl import ParagraphRepository

class ParagraphService:
    def __init__(self, mongo_config):
        self.paragraph_repository = ParagraphRepository(mongo_config)

    def insert_paragraph(self, paragraph):
        self.paragraph_repository.insert_paragraph(paragraph)
        return True, "Documento inserido com sucesso!"

    def count_paragraphs_by_doc_id(self, doc_id):
        """ Conta o número de parágrafos por doc_id """
        return self.paragraph_repository.count_paragraphs_by_doc_id(doc_id)
    
    def list_paragraphs_by_doc_id(self, doc_id):
        """ Obtém os paragrafos com um doc_id"""
        return self.paragraph_repository.list_paragraphs_by_doc_id(doc_id)
    
    def get_paragraph_content(self, document_id, num_paragraph):
        return self.paragraph_repository.get_paragraph_content(document_id, num_paragraph)

    def update_paragraph_translation(self, document_id, num_paragraph, translation):
        return self.paragraph_repository.update_paragraph_translation(document_id, num_paragraph, translation)

    def get_paragraph_translated(self, document_id, num_paragraph):
        return self.paragraph_repository.get_paragraph_translated(document_id, num_paragraph)