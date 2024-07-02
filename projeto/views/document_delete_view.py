from projeto.views.base_view import BaseView


class DocumentDeleteView(BaseView):
    def __init__(self, view_manager, document):
        super().__init__(view_manager)
        self.document = document

    def display(self):
        confirmacao = input("\nTem certeza que deseja deletar este documento? (s/n): ")
        if confirmacao.lower() == 's':
            success, message = self.get_doc_controller().delete_document(self.document._id)
            if success:
                print(f'\n{message}')
                input("Pressione Enter para voltar à lista de documentos...")
                return self.view_manager.get_view('DocumentListView')
            else:
                print(f"Erro ao deletar documento: {message}")
                input("Pressione Enter para voltar aos detalhes do documento...")
                return self.view_manager.get_view('DocumentDetailView', self.document)
        else:
            return self.view_manager.get_view('DocumentDetailView', self.document)