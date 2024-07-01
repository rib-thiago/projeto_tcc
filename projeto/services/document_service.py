from projeto.persistence.mongodb.document_repository_impl import DocumentRepository

class DocumentService:
    def __init__(self, mongo_config):
        self.document_repository = DocumentRepository(mongo_config)

    def insert_document(self, document):
        try:
            documentos_existentes = self.document_repository.list_documents()
            for doc in documentos_existentes:
                if doc.title == document.title:
                    raise ValueError("Já existe um documento com este título.")
            self.document_repository.insert_document(document)
            return True, "Documento inserido com sucesso!"
        except ValueError as ve:
            return False, str(ve)
        except Exception as e:
            return False, f"Erro ao inserir documento: {e}"

    def update_document(self, document_id, field, new_value):
        modified_count = self.document_repository.update_document(document_id, field, new_value)
        if modified_count > 0:
            return True, "Documento atualizado com sucesso."
        else:
            return False, "Documento não encontrado ou valor já existente."

    def list_documents(self):
        """ Lista todos os documentos """
        return self.document_repository.list_documents()

    def delete_document(self, document_id):
        deleted_count = self.document_repository.delete_document(document_id)
        if deleted_count > 0:
            return True, "Documento deletado com sucesso."
        else:
            return False, "Documento não encontrado."

    def get_document_by_id(self, document_id):
        return self.document_repository.get_document_by_id(document_id)

