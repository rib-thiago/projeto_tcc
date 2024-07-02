class DocumentDetailView:
    def __init__(self, doc_controller, para_controller, documento):
        self.doc_controller = doc_controller
        self.para_controller = para_controller
        self.documento = documento

    def display(self):
        from projeto.views.document_content_view import DocumentContentView
        from projeto.views.document_update_view import DocumentUpdateView
        from projeto.views.document_delete_view import DocumentDeleteView
        from projeto.views.main_menu_view import MainMenuView
        print("\nDetalhes do Documento:\n")
        print(self.documento)
        
        print("\nEscolha uma opção:\n")
        print("1. Visualizar Texto do Documento")
        print("2. Atualizar Documento")
        print("3. Deletar Documento")
        print("4. Voltar ao Menu Principal\n")
        opcao = input("Opção: ")

        if opcao == '1':
            return DocumentContentView(self.doc_controller, self.para_controller, self.documento)
        elif opcao == '2':
            return DocumentUpdateView(self.doc_controller, self.para_controller, self.documento)
        elif opcao == '3':
            return DocumentDeleteView(self.doc_controller, self.para_controller, self.documento)
        elif opcao == '4':
            input("Pressione Enter para voltar ao menu principal...")
            return MainMenuView(self.doc_controller, self.para_controller) 

        else:
            print("Opção inválida. Retornando ao menu principal.")

