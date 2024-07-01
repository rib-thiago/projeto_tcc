# utils/text_utils.py
from projeto.utils.file_handlers import read_file

def extract_text(filepath):
    # Implemente a lógica para extrair texto do conteúdo do arquivo (exemplo básico)
    file_content = read_file(filepath)
    return file_content

def extract_paragraphs(text_content):
    # Implemente a lógica para extrair parágrafos do texto (exemplo básico)
    return text_content.split('\n\n')  # Exemplo simples, pode ser mais robusto dependendo da estrutura do texto
