from itertools import islice
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from projeto.views.base_view import BaseView
from bson import ObjectId

class DocumentParagraphListView(BaseView):
    def __init__(self, view_manager, documento, start_paragraph=0, paragraphs_per_page=5):
        super().__init__(view_manager)
        self.documento = documento
        self.start_paragraph = start_paragraph
        self.paragraphs_per_page = paragraphs_per_page

    def display(self):
        console = Console()
        doc_id = self.documento._id
        contents = self.get_para_controller().list_paragraphs(doc_id)
        total_paragraphs = len(contents)

        while self.start_paragraph < total_paragraphs:
            end_paragraph = self.start_paragraph + self.paragraphs_per_page
            current_paragraphs = list(islice(contents, self.start_paragraph, end_paragraph))

            console.clear()

            # Constrói o texto formatado para exibir os parágrafos
            list_text = Text()
            list_text.append("\n")
            list_text.append(f"Exibindo {self.start_paragraph + 1} a {min(end_paragraph, total_paragraphs)} de {total_paragraphs} parágrafos\n\n")
            for para in current_paragraphs:
                para_id = para._id
                list_text.append(f"Parágrafo - {para_id}\n")

            # Renderiza o painel com os parágrafos formatados
            console.print(Panel(list_text, title='Lista de Parágrafos', style="green on black", width=100))

            # Constrói o painel com as opções de navegação
            options_text = Text()
            options_text.append("\n")
            options_text.append("[1] Voltar aos detalhes do documento", style="bold")
            options_text.append("\n")
            options_text.append("[2] Ver mais parágrafos", style="bold")
            if self.start_paragraph > 0:
                options_text.append("\n")
                options_text.append("[3] Voltar para parágrafos anteriores", style="bold")
            options_text.append("\n")
            options_text.append("\nVisualizar um ou mais parágrafos (s):", style='bold')

            console.print(Panel(options_text, title="Opções", style="green on black", width=100))

            opcao = input("> ")

            if opcao == '1':
                return self.view_manager.get_view('DocumentDetailView', self.documento)
            elif opcao == '2':
                self.start_paragraph = end_paragraph
            elif opcao == '3' and self.start_paragraph > 0:
                self.start_paragraph -= self.paragraphs_per_page
                if self.start_paragraph < 0:
                    self.start_paragraph = 0
            elif opcao == 's':
                selected_paragraphs = self.prompt_paragraph_selection()
                if selected_paragraphs:
                    return self.view_manager.get_view('ParagraphDetailView', self.documento, selected_paragraphs)
            else:
                print("Opção inválida.")

        print("Você já visualizou todos os parágrafos.")
        input("\nPressione Enter para voltar aos detalhes do documento.")
        return self.view_manager.get_view('DocumentDetailView', self.documento)

    def prompt_paragraph_selection(self):
        """ Método para solicitar a seleção de parágrafos do usuário """
        console = Console()
        selected_paragraphs = []
        while True:
            console.print(Panel("Digite o número do parágrafo ou um intervalo separado por vírgula (Ex: 1, 3-5): ", style="green on black", width=100))
            paragraph_input = input(" ")
            parts = paragraph_input.split(',')
            for part in parts:
                if '-' in part:
                    start, end = map(int, part.split('-'))
                    selected_paragraphs.extend(map(str, range(start, end + 1)))
                else:
                    selected_paragraphs.append(str(int(part)))
            
            confirmation_text = f"\nVocê selecionou os parágrafos: {selected_paragraphs}. Deseja continuar? (s/n): "
            console.print(Panel(confirmation_text, style="green on black", width=100))
            confirm_input = input(" ")

            if confirm_input.lower() == 's':
                return selected_paragraphs
            else:
                selected_paragraphs = []

