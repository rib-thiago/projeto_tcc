from projeto.views.base_view import BaseView
from textwrap import fill

class ParagraphDetailView(BaseView):
    def __init__(self, view_manager, documento, selected_paragraphs):
        super().__init__(view_manager)
        self.documento = documento
        self.selected_paragraphs = selected_paragraphs
        self.doc_id = documento._id
        self.total_paragraphs = len(selected_paragraphs)
        self.current_index = 0

    def display(self):
        while self.current_index < self.total_paragraphs:
            num_paragraph = self.selected_paragraphs[self.current_index]
            self.display_paragraph(num_paragraph)
            option = self.get_user_option()
            if option == '1':
                self.current_index += 1
            elif option == '2':
                input("\nPressione Enter para voltar aos detalhes do documento.")
                return self.view_manager.get_view('DocumentDetailView', self.documento._id)
            elif option == '3':
                paragraph_to_translate = self.selected_paragraphs[self.current_index]
                return self.view_manager.get_view('TranslateParagraphView', self.documento, paragraph_to_translate)
            elif option == '4' and self.current_index > 0:
                self.current_index -= 1
            else:
                print("Opção inválida.")

        print("Você já visualizou todos os parágrafos.")
        input("\nPressione Enter para voltar aos detalhes do documento.")
        return self.view_manager.get_view('DocumentDetailView', self.documento._id)

    def display_paragraph(self, num_paragraph):
        paragraph_text = self.get_para_controller().get_paragraph_content(self.doc_id, num_paragraph)
        translated, translated_content = self.get_para_controller().get_paragraph_translated(self.doc_id, num_paragraph)

        print(f"\nVisualizando Parágrafo {num_paragraph}:\n")
        wrapped_paragraph = fill(paragraph_text, width=80)  # Aplica soft wrapping ao texto
        print(wrapped_paragraph + "\n")

        if translated:
            wrapped_translated = fill(translated_content, width=80 )
            print(f"Tradução:\n{wrapped_translated}\n")

    def get_user_option(self):
        print("Escolha uma opção:")
        print("[1] Próximo parágrafo")
        print("[2] Voltar aos detalhes do documento")
        print("[3] Traduzir parágrafo")

        if self.current_index > 0:
            print("[4] Parágrafo anterior")

        return input("> ")
