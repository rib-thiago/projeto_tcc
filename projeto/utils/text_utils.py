# utils/text_utils.py
from projeto.utils.file_handlers import read_file

def extract_text(filepath):
    # Implemente a lógica para extrair texto do conteúdo do arquivo (exemplo básico)
    file_content = read_file(filepath)
    return file_content

def extract_paragraphs(text):
        paragraphs = text.split('\n\n')
        return [para.strip() for para in paragraphs if para.strip()]

