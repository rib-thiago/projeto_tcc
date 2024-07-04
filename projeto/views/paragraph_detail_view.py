from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from projeto.views.base_view import BaseView

class ParagraphDetailView(BaseView):
    def __init__(self, view_manager, documento, selected_paragraphs):
        super().__init__(view_manager)
        self.documento = documento
        self.selected_paragraphs = selected_paragraphs

    def display(self):
        console = Console()
        paragraphs = self.selected_paragraphs
        doc_id = self.documento._id  # Certifique-se de que _id é acessado corretamente
        
        start_paragraph = 0
        paragraphs_per_page = 5

        while start_paragraph < len(paragraphs):
            end_paragraph = start_paragraph + paragraphs_per_page
            current_paragraphs = paragraphs[start_paragraph:end_paragraph]

            # Constrói o texto formatado para exibir os parágrafos
            text = Text()
            for idx, num_paragraph in enumerate(current_paragraphs, start=start_paragraph + 1):
                # Obtém o conteúdo do parágrafo usando o controlador de parágrafo
                paragraph_text = self.get_para_controller().get_paragraph_content(doc_id, num_paragraph)
                # Adiciona uma linha ao texto formatado para o parágrafo atual
                text.append(f"Parágrafo {num_paragraph}:\n", style="bold green")
                text.append(paragraph_text + "\n\n")

            # Renderiza o painel com os parágrafos formatados
            console.print(Panel(text, title="Visualizando Parágrafos Selecionados", style="green on black", width=100))

            # Constrói o painel com as opções de navegação
            options_text = Text()
            options_text.append("\n")
            options_text.append("[1] Ver mais parágrafos", style="bold")
            options_text.append("\n")
            options_text.append("[2] Voltar aos detalhes do documento", style="bold")
            if start_paragraph > 0:
                options_text.append("\n")
                options_text.append("[3] Voltar para parágrafos anteriores", style="bold")

            console.print(Panel(options_text, title="Opções", style="green on black", width=100))

            opcao = input("> ")

            if opcao == '1':
                start_paragraph = end_paragraph
            elif opcao == '2':
                input("\nPressione Enter para voltar aos detalhes do documento.")
                return self.view_manager.get_view('DocumentDetailView', self.documento)
            elif opcao == '3' and start_paragraph > 0:
                start_paragraph -= paragraphs_per_page
                if start_paragraph < 0:
                    start_paragraph = 0
            else:
                console.print("Opção inválida.")

        console.print("Você já visualizou todos os parágrafos.")
        input("\nPressione Enter para voltar aos detalhes do documento.")
        return self.view_manager.get_view('DocumentDetailView', self.documento)
