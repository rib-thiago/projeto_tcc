from projeto.views.base_view import BaseView

class DocumentUpdateView(BaseView):
    def __init__(self, view_manager, document):
        super().__init__(view_manager)
        self.document = document

    def display(self):
        while True:
            field = input("\nInforme o campo a ser atualizado (ex. title, author, language): ")
            
            if field in ["paragraphs", "num_paragraphs"]:
                print("Erro: Não é permitido editar o campo 'paragraphs' ou 'num_paragraphs'.")
                continue
            
            new_value = input(f"\nInforme o novo valor para o campo {field}: ")
            success, message = self.get_doc_controller().update_document(self.document._id, field, new_value)
            
            if success:
                print("\nDocumento atualizado com sucesso:\n")
            else:
                print(f"Erro: {message}")

            input("Pressione Enter para voltar à lista de documentos...")
            return self.view_manager.get_view('DocumentListView')
