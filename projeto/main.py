# main.py

from projeto.persistence.mongodb.mongodb_config import MongoDBConfig
from projeto.controllers.document_controller import DocumentController
from projeto.controllers.paragraph_controller import ParagraphController
from projeto.tui import TUI

def main():
    # Configuração do MongoDB
    mongodb_config = MongoDBConfig(uri='mongodb+srv://admin:qwert@cluster0.avisr7t.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
    mongodb_config.connect()
    # Inicialização do Repositório
    documents_collection = mongodb_config.get_collection('documents')
    paragraphs_collection = mongodb_config.get_collection('paragraphs')

    # Inicialização da TUI
    doc_controller = DocumentController(mongodb_config)
    para_controller = ParagraphController(mongodb_config)
    app = TUI(doc_controller, para_controller)
    app.run()

if __name__ == "__main__":
    main()