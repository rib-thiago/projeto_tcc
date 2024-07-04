from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from projeto.views.base_view import BaseView

class DocumentDetailView(BaseView):
    def __init__(self, view_manager, documento):
        super().__init__(view_manager)
        self.documento = documento

    def display(self):
        console = Console()

        # Exibe os detalhes do documento em uma tabela estilizada
        table = Table(show_header=False, title_style="green on black", style='green on black', width=100, title='Detalhes do Documento:')
        table.add_column(header_style="green on black", width=30)
        table.add_column(header_style="green on black", width=70)

        table.add_row("Título", self.documento.title, style="green on black")
        table.add_row("Autor", self.documento.author, style="green on black")
        table.add_row("Idioma", self.documento.language, style="green on black")
        table.add_row("Filepath", self.documento.filepath, style="green on black")
        table.add_row("Source", self.documento.source, style="green on black")
        table.add_row("Número de Parágrafos", str(self.documento.num_paragraphs), style="green on black")
        # table.add_row("Número de Páginas", str(self.documento.num_pages), style="green on black")
        table.add_row("Data de Criação", self.documento.created_at.strftime("%d/%m/%Y"), style="green on black")

        console.print(table)

        # Constrói o painel com as opções de navegação dinamicamente
        options_text = Text()
        options_text.append("\n")
        options_text.append("[1] Visualizar Texto do Documento", style="bold")
        options_text.append("\n")
        options_text.append("[2] Visualizar Paragráfos do Documento", style="bold")
        options_text.append("\n")
        options_text.append("[3] Atualizar Dados do Documento", style="bold")
        options_text.append("\n")
        options_text.append("[4] Deletar Documento", style="bold")
        options_text.append("\n")
        options_text.append("[5] Voltar ao Menu Principal", style="bold")

        console.print(Panel(options_text, title="Escolha uma opção", style="green on black", width=100))

        # Recebe a opção escolhida pelo usuário
        opcao = input("> ")

        # Lógica para lidar com a opção escolhida
        if opcao == '1':
            return self.view_manager.get_view('DocumentContentView', self.documento)
        elif opcao == '2':
            return self.view_manager.get_view('DocumentParagraphListView', self.documento)
        elif opcao == '3':
            return self.view_manager.get_view('DocumentUpdateView', self.documento)
        elif opcao == '4':
            return self.view_manager.get_view('DocumentDeleteView', self.documento)
        elif opcao == '5':
            console.print(Panel(f'Pressione Enter para voltar à lista de documentos...', style="green on black", width=100))
            input("")
            return self.view_manager.get_view('MainMenuView')
        else:
            console.print(Panel(f'Opção inválida, pressione enter para retornar ao menu', style="red on black", width=100))
            input("")
            return self.view_manager.get_view('MainMenuView')
