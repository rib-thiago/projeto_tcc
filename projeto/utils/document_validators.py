# utils/validators.py
import os

class DocumentValidator:
    @staticmethod
    def validate(document, existing_documents=None):
        errors = []
        errors += DocumentValidator.validate_file_path(document.filepath)
        errors += DocumentValidator.validate_file_type(document.filepath)
        errors += DocumentValidator.validate_document_title(document.title, existing_documents)

        return errors

    @staticmethod
    def validate_file_path(file_path):
        errors = []
        absolute_path = os.path.abspath(file_path)

        if not os.path.isfile(absolute_path):
            errors.append(f'O caminho {file_path} não aponta para um arquivo válido.')
        
        return errors

    @staticmethod
    def validate_file_type(file_path):
        errors = []
        absolute_path = os.path.abspath(file_path)
        file_extension = os.path.splitext(absolute_path)[1].lower()

        if file_extension not in ['.txt', '.pdf']:
            errors.append('Formato de arquivo não suportado. Apenas .txt e .pdf são permitidos.')
        
        return errors
    
    @staticmethod
    def validate_document_title(title, existing_documents):
        errors = []
        if existing_documents is not None:
            for doc in existing_documents:
                if doc.title == title:
                    errors.append("Já existe um documento com este título.")
        return errors



