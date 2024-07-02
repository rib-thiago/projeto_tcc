from projeto.views.base_view import BaseView

class DocumentListView(BaseView):
    def display(self):
        documents = self.get_doc_controller().list_documents()

        print("\n=== Lista de Documentos ===")
        for idx, doc in enumerate(documents):
            print(f"{idx + 1}. {doc.title}")

        escolha = input("\nEscolha um documento pelo número ou pressione Enter para voltar: ")

        if escolha.isdigit() and 1 <= int(escolha) <= len(documents):
            escolha_idx = int(escolha) - 1
            return self.view_manager.get_view('DocumentDetailView', documents[escolha_idx])
        else:
            return self.view_manager.get_view('MainMenuView')
