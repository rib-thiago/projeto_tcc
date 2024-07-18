from projeto.views.base_view import BaseView

class DocumentInsertView(BaseView):
    def display(self):
        print("\n")
        print("=== Inserir Novo Documento ===\n")

        title = input("Título do Documento: ")
        author = input("Autor do Documento: ")
        language = input("Idioma do Documento: ")
        filepath = input("Path do Arquivo de Documento: ")
        source = input("URL da fonte do Documento, se aplicável: ")

        success, message = self.get_doc_controller().insert_document(title, author, language, filepath, source)

        if success:
            print(f'\n{message}')
        else:
            input(f"Erro ao inserir documento: {message}")
            return self.view_manager.get_view('DocumentInsertView')

        input("Pressione Enter para voltar ao menu principal...")
        return self.view_manager.get_view('MainMenuView')
