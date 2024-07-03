from itertools import islice
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from projeto.utils.text_utils import extract_paragraphs
from projeto.views.base_view import BaseView

class DocumentContentView(BaseView):
    def __init__(self, view_manager, document, start_paragraph=0, paragraphs_per_page=5):
        super().__init__(view_manager)
        self.document = document
        self.start_paragraph = start_paragraph
        self.paragraphs_per_page = paragraphs_per_page

    def display(self):
        console = Console()

        paragraphs = extract_paragraphs(self.document.text)
        total_paragraphs = len(paragraphs)

        while self.start_paragraph < total_paragraphs:
            end_paragraph = self.start_paragraph + self.paragraphs_per_page
            current_paragraphs = list(islice(paragraphs, self.start_paragraph, end_paragraph))

            console.clear()

            # Constrói o texto formatado para exibir os parágrafos
            text = Text()
            for idx, paragraph in enumerate(current_paragraphs, start=self.start_paragraph + 1):
                text.append(f"Parágrafo {idx}:\n", style="bold green")
                text.append(paragraph + "\n\n")

            # Renderiza o painel com os parágrafos formatados
            console.print(Panel.fit(text, title="Visualizando Parágrafos", style="green on black", width=100))

            # Constrói o painel com as opções de navegação
            options_text = Text()
            options_text.append("\n")
            options_text.append("[1] Ver mais parágrafos", style="bold")
            options_text.append("\n")
            options_text.append("[2] Voltar aos detalhes do documento", style="bold")
            if self.start_paragraph > 0:
                options_text.append("\n")
                options_text.append("[3] Voltar para parágrafos anteriores", style="bold")

            console.print(Panel(options_text, title="Opções", style="green on black", width=100))

            opcao = input("> ")

            if opcao == '1':
                self.start_paragraph = end_paragraph
            elif opcao == '2':
                input("\nPressione Enter para voltar aos detalhes do documento.")
                return self.view_manager.get_view('DocumentDetailView', self.document)
            elif opcao == '3' and self.start_paragraph > 0:
                self.start_paragraph -= self.paragraphs_per_page
                if self.start_paragraph < 0:
                    self.start_paragraph = 0
            else:
                print("Opção inválida.")

        print("Você já visualizou todos os parágrafos.")
        input("\nPressione Enter para voltar aos detalhes do documento.")
        return self.view_manager.get_view('DocumentDetailView', self.document)
