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