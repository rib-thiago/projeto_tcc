from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from projeto.views.base_view import BaseView

class DocumentDeleteView(BaseView):
    def __init__(self, view_manager, document):
        super().__init__(view_manager)
        self.document = document

    def display(self):
        console = Console()

        while True:
            # Exibe as informações atuais do documento
            table = Table(show_header=False, title_style="green on black", style='green on black', width=100, title='Atualizar Documento:')
            table.add_column(header_style="green on black", width=30)
            table.add_column(header_style="green on black", width=70)

            table.add_row("Título", self.document.title, style="green on black")
            table.add_row("Autor", self.document.author, style="green on black")
            table.add_row("Idioma", self.document.language, style="green on black")
            table.add_row("Filepath", self.document.filepath, style="green on black")
            table.add_row("Source", self.document.source, style="green on black")
            table.add_row("Número de Parágrafos", str(self.document.num_paragraphs), style="green on black")
            table.add_row("Data de Criação", self.document.created_at.strftime("%d/%m/%Y"), style="green on black")

            console.print(table)

            # Renderiza opção para confirmar a deleção
            confirmar_delecao = Text()
            confirmar_delecao.append("\nTem certeza que deseja deletar este documento? (s/n)", style="bold")
            console.print(Panel(confirmar_delecao, title="Deletar Documento", style="green on black", width=100))

            confirmacao = input("> ")

            if confirmacao.lower() == 's':
                success, message = self.get_doc_controller().delete_document(self.document._id)
                if success:
                    console.print(Panel(f'\n{message}\n\nPressione Enter para voltar à lista de documentos...', style="green on black", width=100))
                    input("")
                    return self.view_manager.get_view('DocumentListView')
                else:
                    console.print(Panel(f"Erro ao deletar documento: {message}\n\nPressione Enter para voltar à lista de documentos...", title="Erro", style="red on black", width=100))
                    input("")
                    return self.view_manager.get_view('DocumentDetailView', self.document)
            elif confirmacao.lower() == 'n':
                return self.view_manager.get_view('DocumentDetailView', self.document)
            else:
                console.print(Panel(f'Opção inválida! Pressione Enter para retornar ao Menu', style="red on black", width=100))
                input("")
                return self.view_manager.get_view('DocumentDetailView', self.document)

