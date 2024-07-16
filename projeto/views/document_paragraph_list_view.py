from itertools import islice
from projeto.views.base_view import BaseView
from bson import ObjectId

class DocumentParagraphListView(BaseView):
    def __init__(self, view_manager, documento, start_paragraph=0, paragraphs_per_page=10):
        super().__init__(view_manager)
        self.documento = documento
        self.start_paragraph = start_paragraph
        self.paragraphs_per_page = paragraphs_per_page

    def display(self):
        doc_id = self.documento._id
        all_paragraphs = self.get_para_controller().list_paragraphs(doc_id)

        # Filtragem dos parágrafos
        filtered_paragraphs = self.filter_paragraphs(all_paragraphs)

        total_paragraphs = len(filtered_paragraphs)

        while self.start_paragraph < total_paragraphs:
            end_paragraph = self.start_paragraph + self.paragraphs_per_page
            current_paragraphs = list(islice(filtered_paragraphs, self.start_paragraph, end_paragraph))

            # Exibe os parágrafos formatados
            print("\nLista de Parágrafos:\n")
            print(f"Exibindo {self.start_paragraph + 1} a {min(end_paragraph, total_paragraphs)} de {total_paragraphs} parágrafos\n")
            for paragraph in current_paragraphs:
                self.print_paragraph_info(paragraph)
            
            # Espaçamento entre lista de parágrafos e menu de opções
            print("\n")

            # Exibe as opções de navegação
            self.print_navigation_options()
            opcao = input("> ")

            if opcao == '1':
                return self.view_manager.get_view('DocumentDetailView', self.documento)
            elif opcao == '2':
                self.start_paragraph = end_paragraph
            elif opcao == '3':
                selected_paragraphs = self.prompt_paragraph_selection()
                if selected_paragraphs:
                    return self.view_manager.get_view('ParagraphDetailView', self.documento, selected_paragraphs)            
            elif opcao == '4':
                return self.view_manager.get_view('DocumentParagraphListView', self.documento)
            elif opcao == '5' and self.start_paragraph > 0:
                self.start_paragraph -= self.paragraphs_per_page
                if self.start_paragraph < 0:
                    self.start_paragraph = 0
            else:
                print("Opção inválida.")

        print("Você já visualizou todos os parágrafos.")
        input("\nPressione Enter para voltar aos detalhes do documento.")
        return self.view_manager.get_view('DocumentDetailView', self.documento)

    def prompt_paragraph_selection(self):
        """ Método para solicitar a seleção de parágrafos do usuário """
        selected_paragraphs = []
        while True:
            print("\n Digite o número do parágrafo ou um intervalo separado por vírgula (Ex: 1, 3-5): ")
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

    def filter_paragraphs(self, paragraphs):
        """ Filtra os parágrafos com base nas preferências do usuário """
        print("Escolha o tipo de parágrafos a serem listados:")
        print("[1] Todos os parágrafos")
        print("[2] Apenas parágrafos traduzidos")
        print("[3] Apenas parágrafos não traduzidos")

        option = input("> ")

        if option == '1':
            return paragraphs
        elif option == '2':
            return [para for para in paragraphs if para.translated]
        elif option == '3':
            return [para for para in paragraphs if not para.translated]
        else:
            print("Opção inválida. Listando todos os parágrafos por padrão.")
            return paragraphs

    def print_paragraph_info(self, paragraph):
        """ Exibe informações formatadas sobre um parágrafo """
        para_num = paragraph.num_paragraph
        para_translated = paragraph.translated
        translated_status = "Traduzido" if para_translated else "Não traduzido"
        print(f"Parágrafo nº {para_num} - {translated_status}")

    def print_navigation_options(self):
        """ Exibe as opções de navegação """
        print("Escolha uma opção:")
        print("[1] Voltar aos detalhes do documento")
        print("[2] Ver mais parágrafos")
        print("[3] Visualizar um ou mais parágrafos:")
        print("[4] Filtrar lista de parágrafos")        
        if self.start_paragraph > 0:
            print("[5] Voltar para parágrafos anteriores")
        