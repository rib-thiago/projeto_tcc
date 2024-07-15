from projeto.views.base_view import BaseView

class DocumentDeleteView(BaseView):
    def __init__(self, view_manager, document):
        super().__init__(view_manager)
        self.document = document

    def display(self):
        while True:
            # Exibe as informações atuais do documento
            print("\nDeletar Documento:\n")
            print(f"Título: {self.document.title}")
            print(f"Autor: {self.document.author}")
            print(f"Idioma: {self.document.language}")
            print(f"Filepath: {self.document.filepath}")
            print(f"Source: {self.document.source}")
            print(f"Número de Parágrafos: {self.document.num_paragraphs}")
            print(f"Data de Criação: {self.document.created_at.strftime('%d/%m/%Y')}")

            # Renderiza opção para confirmar a deleção
            confirmacao = input("\nTem certeza que deseja deletar este documento? (s/n): ")

            if confirmacao.lower() == 's':
                success, message = self.get_doc_controller().delete_document(self.document._id)
                if success:
                    print(f'\n{message}\n')
                    input("Pressione Enter para voltar à lista de documentos...")
                    return self.view_manager.get_view('DocumentListView')
                else:
                    print(f"Erro ao deletar documento: {message}")
                    input("Pressione Enter para voltar à lista de documentos...")
                    return self.view_manager.get_view('DocumentDetailView', self.document)
            elif confirmacao.lower() == 'n':
                return self.view_manager.get_view('DocumentDetailView', self.document)
            else:
                print('Opção inválida!')

