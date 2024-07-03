from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from projeto.views.base_view import BaseView

class DocumentListView(BaseView):
    def display(self):
        console = Console()
        documents = self.get_doc_controller().list_documents()

        # Construir painel com a lista de documentos
        list_text = Text()
        list_text.append("\n")
        for idx, doc in enumerate(documents):
            list_text.append(f"{idx + 1}. {doc.title}\n")

        list_text.append("\n")
        list_text.append("Escolha um documento pelo número ou pressione Enter para voltar: ", style="bold")

        console.print(Panel(list_text, title='Lista de Documentos', style="green on black", width=100))
        escolha = input(" ")

        if escolha.isdigit() and 1 <= int(escolha) <= len(documents):
            escolha_idx = int(escolha) - 1
            return self.view_manager.get_view('DocumentDetailView', documents[escolha_idx])
        else:
            return self.view_manager.get_view('MainMenuView')
