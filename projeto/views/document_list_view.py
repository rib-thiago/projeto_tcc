from projeto.views.base_view import BaseView

class DocumentListView(BaseView):
    def display(self):
        documents = self.get_doc_controller().list_documents()

        print(f'=== Lista de Arquivos ===')

        # Construir lista de documentos
        print("\n")
        for idx, doc in enumerate(documents):
            print(f"{idx + 1}. {doc.title}")

        print("\n")
        escolha = input("Escolha um documento pelo número ou pressione Enter para voltar: ")

        if escolha.isdigit() and 1 <= int(escolha) <= len(documents):
            escolha_idx = int(escolha) - 1
            document_id = documents[escolha_idx]._id
            return self.view_manager.get_view('DocumentDetailView', document_id)
        else:
            return self.view_manager.get_view('MainMenuView')




