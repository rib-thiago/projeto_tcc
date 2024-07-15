from itertools import islice
from projeto.views.base_view import BaseView
from bson import ObjectId

class DocumentParagraphListView(BaseView):
    def __init__(self, view_manager, documento, start_paragraph=0, paragraphs_per_page=5):
        super().__init__(view_manager)
        self.documento = documento
        self.start_paragraph = start_paragraph
        self.paragraphs_per_page = paragraphs_per_page

    def display(self):
        doc_id = self.documento._id
        contents = self.get_para_controller().list_paragraphs(doc_id)
        total_paragraphs = len(contents)

        while self.start_paragraph < total_paragraphs:
            end_paragraph = self.start_paragraph + self.paragraphs_per_page
            current_paragraphs = list(islice(contents, self.start_paragraph, end_paragraph))

            # Exibe os parágrafos formatados
            print("\nLista de Parágrafos:\n")
            print(f"Exibindo {self.start_paragraph + 1} a {min(end_paragraph, total_paragraphs)} de {total_paragraphs} parágrafos\n")
            for para in current_paragraphs:
                para_id = para._id
                print(f"Parágrafo - {para_id}\n")

            # Exibe as opções de navegação
            print("Escolha uma opção:")
            print("[1] Voltar aos detalhes do documento")
            print("[2] Ver mais parágrafos")
            if self.start_paragraph > 0:
                print("[3] Voltar para parágrafos anteriores")
            print("\nVisualizar um ou mais parágrafos (s):")

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
        selected_paragraphs = []
        while True:
            print("Digite o número do parágrafo ou um intervalo separado por vírgula (Ex: 1, 3-5): ")
            paragraph_input = input(" ")
            parts = paragraph_input.split(',')
            for part in parts:
                if '-' in part:
                    start, end = map(int, part.split('-'))
                    selected_paragraphs.extend(map(str, range(start, end + 1)))
                else:
                    selected_paragraphs.append(str(int(part)))
            
            confirmation_text = f"\nVocê selecionou os parágrafos: {selected_paragraphs}. Deseja continuar? (s/n): "
            print(confirmation_text)
            confirm_input = input(" ")

            if confirm_input.lower() == 's':
                return selected_paragraphs
            else:
                selected_paragraphs = []
