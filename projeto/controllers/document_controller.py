from projeto.services.document_service import DocumentService
from projeto.models.document import Document

class DocumentController:
    def __init__(self, mongo_config):
        self.document_service = DocumentService(mongo_config)

    def insert_document(self, titulo, autor, idioma):
        """ Insere um novo documento """
        document = Document(titulo, autor, idioma)
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