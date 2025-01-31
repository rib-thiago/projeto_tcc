from projeto.views.base_view import BaseView
from projeto.utils.file_handlers import verify_file_path

class DocumentInsertView(BaseView):
    def display(self):
        print("\n")
        print("=== Inserir Novo Documento ===\n")

        title = input("Título do Documento: ")
        author = input("Autor do Documento: ")
        language = input("Idioma do Documento: ")
        filepath = input("Path do Arquivo de Documento: ")
        # filepath = verify_file_path(path)
        source = input("URL da fonte do Documento, se aplicável: ")

        success, message = self.get_doc_controller().insert_document(title, author, language, filepath, source)

        if success:
            print(f'\n{message}')
        else:
            print(f"Erro ao inserir documento: {message}")

        input("Pressione Enter para voltar ao menu principal...")
        return self.view_manager.get_view('MainMenuView')
