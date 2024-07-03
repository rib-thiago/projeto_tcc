from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from projeto.views.base_view import BaseView

class DocumentUpdateView(BaseView):
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

            # Prompt para atualizar um campo específico
            field_prompt = Text()
            field_prompt.append("\nInforme o campo a ser atualizado (ex. title, author, language): ", style="bold")
            console.print(Panel(field_prompt, style="green on black", width=100))
            field = input("> ")

            if field in ["paragraphs", "num_paragraphs"]:
                console.print(Panel("Erro: Não é permitido editar o campo 'paragraphs' ou 'num_paragraphs'.", style="red on black", width=100))
                input("")
                return self.view_manager.get_view('DocumentDetailView', self.document)

            new_value_prompt = Text()
            new_value_prompt.append(f"\nInforme o novo valor para o campo {field}: ", style="bold")
            console.print(Panel(new_value_prompt, style="green on black", width=100))
            new_value = input("> ")

            success, message = self.get_doc_controller().update_document(self.document._id, field, new_value)

            if success:
                console.print(Panel("\nDocumento atualizado com sucesso.", style="green on black", width=100))
            else:
                console.print(Panel(f"Erro: {message}", style="red on black", width=100))
                input("")
                return self.view_manager.get_view('DocumentDetailView', self.document)
            
            console.print(Panel("Pressione Enter para voltar aos detalhes do documentos...", style="green on black", width=100))
            input("")
            return self.view_manager.get_view('DocumentDetailView', self.document)
