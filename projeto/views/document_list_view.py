class DocumentListView:
    def __init__(self, doc_controller):
        self.doc_controller = doc_controller

    def display(self):
        from projeto.views.main_menu_view import MainMenuView
        from projeto.views.document_detail_view import DocumentDetailView
        documentos = self.doc_controller.list_documents()
        print("\nDocumentos Cadastrados:\n")
        for idx, documento in enumerate(documentos):
            print(f'{idx + 1}. {documento.title} - {documento.author}\n')

        escolha = input("\nDigite o número do documento para visualizar mais detalhes ou 'v' para voltar ao menu principal: ")
        
        if escolha.lower() == 'v':
            input("Pressione Enter para voltar ao menu principal...")
            return MainMenuView(self.doc_controller) 
        else:
            try:
                escolha_idx = int(escolha) - 1
                if 0 <= escolha_idx < len(documentos):
                    return DocumentDetailView(self.doc_controller, documentos[escolha_idx])
                else:
                    print("Opção inválida.")
                    return self
            except ValueError:
                print("Entrada inválida.")
                return self
