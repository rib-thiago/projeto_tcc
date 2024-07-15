from itertools import islice
from projeto.utils.text_utils import extract_paragraphs
from projeto.views.base_view import BaseView

class DocumentContentView(BaseView):
    def __init__(self, view_manager, document, start_paragraph=0, paragraphs_per_page=5):
        super().__init__(view_manager)
        self.document = document
        self.start_paragraph = start_paragraph
        self.paragraphs_per_page = paragraphs_per_page

    def display(self):
        paragraphs = extract_paragraphs(self.document.text)
        total_paragraphs = len(paragraphs)

        while self.start_paragraph < total_paragraphs:
            end_paragraph = self.start_paragraph + self.paragraphs_per_page
            current_paragraphs = list(islice(paragraphs, self.start_paragraph, end_paragraph))

            # Exibe os parágrafos formatados
            print("\nVisualizando Parágrafos:\n")
            for idx, paragraph in enumerate(current_paragraphs, start=self.start_paragraph + 1):
                print(f"Parágrafo {idx}:\n")
                print(paragraph + "\n")

            # Exibe as opções de navegação
            print("Escolha uma opção:")
            print("[1] Ver mais parágrafos")
            print("[2] Voltar aos detalhes do documento")
            if self.start_paragraph > 0:
                print("[3] Voltar para parágrafos anteriores")

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
