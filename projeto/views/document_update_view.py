from projeto.views.base_view import BaseView

class DocumentUpdateView(BaseView):
    def __init__(self, view_manager, document):
        super().__init__(view_manager)
        self.document = document

    def display(self):

        while True:
            # Exibe as informações atuais do documento
            print("\nAtualizar Documento:\n")
            print(f"Título: {self.document.title}")
            print(f"Autor: {self.document.author}")
            print(f"Idioma: {self.document.language}")
            print(f"Filepath: {self.document.filepath}")
            print(f"Source: {self.document.source}")
            print(f"Número de Parágrafos: {self.document.num_paragraphs}")
            print(f"Data de Criação: {self.document.created_at.strftime('%d/%m/%Y')}")

            # Prompt para atualizar um campo específico
            print("\nInforme o campo a ser atualizado (ex. title, author, language): ")
            field = input("> ")

            if field in ["paragraphs", "num_paragraphs"]:
                print("\nErro: Não é permitido editar o campo 'paragraphs' ou 'num_paragraphs'.")
                input("")
                return self.view_manager.get_view('DocumentDetailView', self.document)

            print(f"\nInforme o novo valor para o campo {field}: ")
            new_value = input("> ")

            success, message = self.get_doc_controller().update_document(self.document._id, field, new_value)

            if success:
                print("\nDocumento atualizado com sucesso.")
            else:
                print(f"\nErro: {message}")
                input("")
                return self.view_manager.get_view('DocumentDetailView', self.document)
            
            print("\nPressione Enter para voltar aos detalhes do documentos...")
            input("")
            return self.view_manager.get_view('DocumentDetailView', self.document)
