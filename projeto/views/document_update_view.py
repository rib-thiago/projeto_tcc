class DocumentUpdateView:
    def __init__(self, doc_controller, para_controller, documento):
        self.doc_controller = doc_controller
        self.para_controller = para_controller
        self.documento = documento

    def display(self):
        from projeto.views.document_detail_view import DocumentDetailView
        
        while True:
            field = input("\nInforme o campo a ser atualizado (ex. title, author, language): ")
            
            if field in ["paragraphs", "num_paragraphs"]:
                print("Erro: Não é permitido editar o campo 'paragraphs' ou 'num_paragraphs'.")
                continue
            
            new_value = input(f"\nInforme o novo valor para o campo {field}: ")
            success, message = self.doc_controller.update_document(self.documento._id, field, new_value)
            
            if success:
                print("\nDocumento atualizado com sucesso:\n")
                self.documento = self.doc_controller.get_document_by_id(self.documento._id)
                print(f'{self.documento}\n')
            else:
                print(f"Erro: {message}")

            input("Pressione Enter para voltar aos detalhes...")
            return DocumentDetailView(self.doc_controller, self.para_controller, self.documento)
