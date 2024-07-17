from itertools import islice
from textwrap import fill
from projeto.utils.text_utils import extract_paragraphs
from projeto.views.base_view import BaseView

class DocumentContentView(BaseView):
    def __init__(self, view_manager, document, start_paragraph=0, paragraphs_per_page=4, line_width=80):
        super().__init__(view_manager)
        self.document = document
        self.start_paragraph = start_paragraph
        self.paragraphs_per_page = paragraphs_per_page
        self.line_width = line_width  # largura da linha para o soft wrapping
        self.paragraphs = extract_paragraphs(self.document.text)
        self.total_paragraphs = len(self.paragraphs)

    def display(self):
        while self.start_paragraph < self.total_paragraphs:
            end_paragraph = self.start_paragraph + self.paragraphs_per_page
            current_paragraphs = list(islice(self.paragraphs, self.start_paragraph, end_paragraph))

            # Exibe os parágrafos formatados
            self.print_paragraphs(current_paragraphs)

            # Exibe as opções de navegação
            self.print_navigation_options()

            opcao = input("> ")

            if opcao == '1':
                self.start_paragraph = end_paragraph
            elif opcao == '2':
                return self.view_manager.get_view('DocumentDetailView', self.document._id)
            else:
                print("Opção inválida.")

        print("Você já visualizou todos os parágrafos.")
        input("\nPressione Enter para voltar aos detalhes do documento.")
        return self.view_manager.get_view('DocumentDetailView', self.document._id)

    def print_paragraphs(self, paragraphs):
        """ Exibe os parágrafos formatados """
        print("\n")
        for idx, paragraph in enumerate(paragraphs, start=self.start_paragraph + 1):
            wrapped_paragraphs = fill(paragraph, width=self.line_width)
            print(wrapped_paragraphs + "\n")

    def print_navigation_options(self):
        """ Exibe as opções de navegação """
        print("Escolha uma opção:")
        print("[1] Ver mais parágrafos")
        print("[2] Voltar aos detalhes do documento")

    def update_paragraphs(self):
        """ Atualiza a lista de parágrafos """
        self.paragraphs = extract_paragraphs(self.document.text)
        self.total_paragraphs = len(self.paragraphs)
        self.start_paragraph = 0
