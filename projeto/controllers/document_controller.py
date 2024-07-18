from projeto.services.document_service import DocumentService
from projeto.services.ocr_service import ocr_extract_text
from projeto.models.document import Document
from projeto.utils.file_handlers import read_file, split_pdf, pdf_to_images
from projeto.utils.text_utils import extract_paragraphs
from .paragraph_controller import ParagraphController

from projeto.utils.validators import DocumentValidator, ParagraphValidator

import os
import tempfile

class DocumentController:
    def __init__(self, mongo_config, paragraph_repository):
        self.document_service = DocumentService(mongo_config, paragraph_repository)
        self.para_controller = ParagraphController(mongo_config)

    def insert_document(self, title, author, language, filepath, source):
        """ Insere um novo documento """
        document = Document(title, author, language, filepath, source, text=None)
        existing_documents = self.document_service.list_documents()  # Obtém os documentos existentes
        validation_errors = DocumentValidator.validate(document, existing_documents)
        if validation_errors:
            return False, "Validation errors: " + ", ".join(validation_errors)
        
        # Processa o arquivo conforme o tipo
        if document.filepath.endswith('.txt'):
            success, message, text, paragraphs = self._process_txt(filepath)
        elif document.filepath.endswith('.pdf'):
            success, message, text, paragraphs = self._process_pdf(filepath)
        else:
            return False, "Formato de arquivo não suportado. Apenas .txt e .pdf são permitidos."

        if not success:
            return False, message

        document.text = text
        doc_id = document._id

        success, message = self.para_controller.insert_paragraphs(paragraphs, doc_id)
        if not success:
            return False, message
        
        # Conta os parágrafos do documento
        num_paragraphs, translated_paragraphs = self.para_controller.count_paragraphs_by_doc_id(doc_id)
        document.num_paragraphs = num_paragraphs

        success, message = self.document_service.insert_document(document)
        return success, message

    def _process_txt(self, filepath):
        """ Processa arquivos TXT """
        try:
            text = read_file(filepath)
            paragraphs = extract_paragraphs(text)
            return True, '', text, paragraphs
        except Exception as e:
            return False, str(e), '', []

    def _process_pdf(self, filepath):
        try:
            # Diretório temporário para armazenar as páginas divididas e convertidas
            with tempfile.TemporaryDirectory() as temp_dir:
                # Dividir o PDF em páginas individuais
                split_pdf(filepath, temp_dir)
    
                # Converter cada página do PDF em imagens PNG
                image_paths = pdf_to_images(temp_dir, temp_dir)
    
                # Inicializa uma variável para armazenar o texto extraído das imagens
                extracted_text = ''
    
                # Processa cada imagem para extrair texto usando OCR
                for image_path in image_paths:
                    extracted_text += ocr_extract_text(image_path) + '\n\n'
    
                # Divide o texto extraído em parágrafos
                paragraphs = extract_paragraphs(extracted_text)
    
                return True, "PDF processado com sucesso", extracted_text, paragraphs
    
        except Exception as e:
            return False, f"Erro ao processar o PDF: {e}", "", []

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