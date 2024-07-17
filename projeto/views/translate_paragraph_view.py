from projeto.views.base_view import BaseView
from textwrap import fill

class TranslateParagraphView(BaseView):
    def __init__(self, view_manager, documento, paragraph_number):
        super().__init__(view_manager)
        self.documento = documento
        self.paragraph_number = paragraph_number

    def display(self):
        doc_id = self.documento._id
        paragraph_number = self.paragraph_number

        # Obtém o conteúdo do parágrafo usando o controlador de parágrafo
        paragraph_text = self.get_para_controller().get_paragraph_content(doc_id, paragraph_number)
        
        print(f"Parágrafo {paragraph_number}:\n")
        wrapped_paragraph = fill(paragraph_text, width=80)  # Aplica soft wrapping ao texto
        print(wrapped_paragraph + "\n")

        source_lang = input("Digite o idioma de origem (por exemplo, 'en' para inglês): ")
        target_lang = input("Digite o idioma de destino (por exemplo, 'pt' para português): ")

        translated = self.get_para_controller().translate_paragraph(paragraph_text, source_lang, target_lang)
        wrapped_translated = fill(translated, width=80)
        print(f'\nTradução: \n{wrapped_translated}')

        save_translation = input(f"\nDeseja salvar essa tradução? (s/n): ").strip().lower()
        if save_translation == 's':
            self.get_para_controller().update_paragraph_translation(doc_id, paragraph_number, translated)

        input("\nPressione Enter para voltar à visualização de parágrafos.")
        return self.view_manager.get_view('ParagraphDetailView', self.documento, [paragraph_number])
        
