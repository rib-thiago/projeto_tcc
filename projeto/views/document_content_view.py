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

        while True:
            end_paragraph = min(self.start_paragraph + self.paragraphs_per_page, total_paragraphs)
        
            print(f"\nVisualizando parágrafos {self.start_paragraph + 1} a {end_paragraph} de {total_paragraphs}\n")
            for i in range(self.start_paragraph, end_paragraph):
                print(paragraphs[i])


            if end_paragraph >= total_paragraphs:
                print("Você chegou ao final do documento.")
                input("Pressione Enter para voltar aos detalhes do documento.")
                return self.view_manager.get_view('DocumentDetailView', self.document)

            print("1. Ver mais parágrafos")
            print("2. Voltar aos detalhes do documento")
            opcao = input("Opção: ")

            if opcao == '1':
                self.start_paragraph = end_paragraph
                if self.start_paragraph >= total_paragraphs:
                    print("Você já visualizou todos os parágrafos.")
                    input("Pressione Enter para voltar aos detalhes do documento.")
                    return self.view_manager.get_view('DocumentDetailView', self.document)
            elif opcao == '2':
                input("Pressione Enter para voltar aos detalhes do documento.")
                return self.view_manager.get_view('DocumentDetailView', self.document)
            else:
                print("Opção inválida.")