from projeto.persistence.mongodb.mongodb_config import MongoDBConfig
from projeto.persistence.mongodb.document_repository_impl import DocumentRepository
from projeto.persistence.mongodb.paragraph_repository_impl import ParagraphRepository

from projeto.controllers.document_controller import DocumentController
from projeto.controllers.paragraph_controller import ParagraphController

from projeto.views.main_menu_view import MainMenuView
from projeto.views.document_insert_view import DocumentInsertView
from projeto.views.document_list_view import DocumentListView
from projeto.views.document_detail_view import DocumentDetailView
from projeto.views.document_update_view import DocumentUpdateView
from projeto.views.document_content_view import DocumentContentView
from projeto.views.document_delete_view import DocumentDeleteView
from projeto.views.document_paragraph_list_view import DocumentParagraphListView
from projeto.views.paragraph_detail_view import ParagraphDetailView
from projeto.views.translate_paragraph_view import TranslateParagraphView
from projeto.view_manager import ViewManager

def main():
    # Configuração do MongoDB
    mongodb_config = MongoDBConfig(uri='mongodb+srv://admin:qwert@cluster0.avisr7t.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
    mongodb_config.connect()
    
    # Inicialização dos Repositórios
    documents_collection = mongodb_config.get_collection('documents')
    paragraphs_collection = mongodb_config.get_collection('paragraphs')

    # Inicializa os repositórios
    paragraph_repository = ParagraphRepository(mongodb_config)
    document_repository = DocumentRepository(mongodb_config, paragraph_repository)

    # Inicialização dos Controllers
    doc_controller = DocumentController(mongodb_config, paragraph_repository)
    para_controller = ParagraphController(mongodb_config)

    # Inicialização do ViewManager
    view_manager = ViewManager(doc_controller, para_controller)
    
    # Registro das Views
    view_manager.register_view('MainMenuView', MainMenuView)
    view_manager.register_view('DocumentInsertView', DocumentInsertView)
    view_manager.register_view('DocumentListView', DocumentListView)
    view_manager.register_view('DocumentDetailView', DocumentDetailView)
    view_manager.register_view('DocumentUpdateView', DocumentUpdateView)
    view_manager.register_view('DocumentContentView', DocumentContentView)
    view_manager.register_view('DocumentDeleteView', DocumentDeleteView)
    view_manager.register_view('DocumentParagraphListView', DocumentParagraphListView)
    view_manager.register_view('ParagraphDetailView', ParagraphDetailView)
    view_manager.register_view('TranslateParagraphView', TranslateParagraphView)
    
    # Iniciar a aplicação com a view inicial
    view_manager.start(view_manager.get_view('MainMenuView'))

if __name__ == "__main__":
    main()
