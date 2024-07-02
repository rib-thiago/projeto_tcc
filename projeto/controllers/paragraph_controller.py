from projeto.services.paragraph_service import ParagraphService
from projeto.models.paragraph import Paragraph


class ParagraphController:
    def __init__(self, mongo_config):
        self.paragraph_service = ParagraphService(mongo_config)

    def insert_paragraphs(self, paragraphs, document_id):
        for num_paragraph, content in enumerate(paragraphs):
            paragraph = Paragraph(document_id=document_id, content=content, num_paragraph=num_paragraph)
            success, message = self.paragraph_service.insert_paragraph(paragraph)
            if not success:
                return False, message
        return True, "All paragraphs inserted successfully"

    def count_paragraphs_by_doc_id(self, doc_id):
        return self.paragraph_service.count_paragraphs_by_doc_id(doc_id)

