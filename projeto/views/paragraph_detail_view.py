from projeto.views.base_view import BaseView

class ParagraphDetailView(BaseView):
    def __init__(self, view_manager, documento, selected_paragraphs):
        super().__init__(view_manager)
        self.documento = documento
        self.selected_paragraphs = selected_paragraphs

    def display(self):
        paragraphs = self.selected_paragraphs
        doc_id = self.documento._id
        
        start_paragraph = 0
        paragraphs_per_page = 5

        while start_paragraph < len(paragraphs):
            end_paragraph = start_paragraph + paragraphs_per_page
            current_paragraphs = paragraphs[start_paragraph:end_paragraph]

            # Exibe os parágrafos formatados
            print("\nVisualizando Parágrafos Selecionados:\n")
            for num_paragraph in current_paragraphs:
                # Obtém o conteúdo do parágrafo usando o controlador de parágrafo
                paragraph_text = self.get_para_controller().get_paragraph_content(doc_id, num_paragraph)
                translated, translated_content = self.get_para_controller().get_paragraph_translated(doc_id, num_paragraph)
                print(f"Parágrafo {num_paragraph}:\n")
                print(paragraph_text + "\n")

                if translated == True:
                    print(f"Tradução: \n {translated_content} \n")

            # Exibe as opções de navegação
            print("Escolha uma opção:")
            print("[1] Ver mais parágrafos")
            print("[2] Voltar aos detalhes do documento")
            print("[3] Traduzir parágrafo")
            if start_paragraph > 0:
                print("[4] Voltar para parágrafos anteriores")

            opcao = input("> ")

            if opcao == '1':
                start_paragraph = end_paragraph
            elif opcao == '2':
                input("\nPressione Enter para voltar aos detalhes do documento.")
                return self.view_manager.get_view('DocumentDetailView', self.documento)
            elif opcao == '3':
                paragraph_to_translate = input(f"Digite o número do parágrafo que deseja traduzir: {current_paragraphs}")
                if paragraph_to_translate in current_paragraphs:
                    return self.view_manager.get_view('TranslateParagraphView', self.documento, paragraph_to_translate)
                else:
                    print("Número de parágrafo inválido.")
            elif opcao == '4' and start_paragraph > 0:
                start_paragraph -= paragraphs_per_page
                if start_paragraph < 0:
                    start_paragraph = 0
            else:
                print("Opção inválida.")

        print("Você já visualizou todos os parágrafos.")
        input("\nPressione Enter para voltar aos detalhes do documento.")
        return self.view_manager.get_view('DocumentDetailView', self.documento)
