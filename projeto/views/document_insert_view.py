class DocumentInsertView:
    def __init__(self, doc_controller):
        self.doc_controller = doc_controller

    def display(self):
        from projeto.views.main_menu_view import MainMenuView
        print("\nInserir Novo Documento\n")
        title = input("Título do Documento: ")
        author = input("Autor do Documento: ")
        language = input("Idioma do Documento: ")
        filepath = input("Path do Arquivo de Documento: ")
        source = input("Url da fonte do Documento, se aplicável: ")
        success, message = self.doc_controller.insert_document(title, author, language, filepath, source)

        if success:
            print(f'\n{message}')
        else:
            print(f"Erro ao inserir documento: {message}")
        
        input("Pressione Enter para voltar ao menu principal...")
        return MainMenuView(self.doc_controller)

