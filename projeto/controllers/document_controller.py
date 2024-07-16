from projeto.services.document_service import DocumentService
from projeto.models.document import Document
from projeto.utils.text_utils import extract_text, extract_paragraphs
from .paragraph_controller import ParagraphController

class DocumentController:
    def __init__(self, mongo_config, paragraph_repository):
        self.document_service = DocumentService(mongo_config, paragraph_repository)
        self.para_controller = ParagraphController(mongo_config)

    def insert_document(self, title, author, language, filepath, source):
        """ Insere um novo documento """
        text = extract_text(filepath)
        paragraphs = extract_paragraphs(text)
        document = Document(title, author, language, filepath, source, text)
        doc_id = document._id
        success, message = self.para_controller.insert_paragraphs(paragraphs, doc_id)
        if not success:
            return False, message
        # Conta os parágrafos do documento
        num_paragraphs, translated_paragraphs = self.para_controller.count_paragraphs_by_doc_id(doc_id)
        document.num_paragraphs = num_paragraphs
        success, message = self.document_service.insert_document(document)
        return success, message



    def list_documents(self):
        """ Lista todos os documentos """
        return self.document_service.list_documents()

    def update_document(self, document_id, field, new_value):
        success, message = self.document_service.update_document(document_id, field, new_value)
        return success, message

    def delete_document(self, document_id):
        success, message = self.document_service.delete_document(document_id)
        return success, message

    def get_document_by_id(self, document_id):
        return self.document_service.get_document_by_id(document_id)