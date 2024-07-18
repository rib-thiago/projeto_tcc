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

class ParagraphValidator:
    @staticmethod
    def validate(paragraph):
        errors = []
        if not paragraph.content:
            errors.append("Content is required.")
        if not paragraph.num_paragraph:
            errors.append("Paragraph number is required.")
        # Adicione mais validações conforme necessário

        return errors




"""
Validação Individual no Controlador: Se você deseja validar apenas o tipo de 
arquivo em um determinado ponto do seu código (por exemplo, antes de chamar o 
serviço de inserção de documento), você pode fazer isso chamando diretamente o 
método validate_file_type do DocumentValidator.

Exemplo:

from utils.validators import DocumentValidator

file_path = 'caminho/do/arquivo.pdf'
errors = DocumentValidator.validate_file_type(file_path)
if errors:
    print("Erros de validação de tipo de arquivo:", errors)
    # Trate os erros conforme necessário

"""

"""
Validação Completa com Instância de Documento: Se você já tem uma instância de 
Document e deseja validar todos os campos, incluindo título, autor, idioma, 
caminho do arquivo e tipo de arquivo, você pode usar o método validate do 
DocumentValidator.

Exemplo:

from utils.validators import DocumentValidator
from projeto.models.document import Document

document = Document(title='Meu Documento', author='Autor', language='pt-br', filepath='caminho/do/arquivo.pdf', source='Fonte')

errors = DocumentValidator.validate(document)
if errors:
    print("Erros de validação:", errors)
    # Trate os erros conforme necessário

"""