from projeto.utils.text_utils import extract_paragraphs


class DocumentContentView:
    def __init__(self, doc_controller, documento, start_paragraph=0, paragraphs_per_page=5):
        self.doc_controller = doc_controller
        self.documento = documento
        self.start_paragraph = start_paragraph
        self.paragraphs_per_page = paragraphs_per_page

    def display(self):
        from projeto.views.document_detail_view import DocumentDetailView
        paragraphs = extract_paragraphs(self.documento.text)
        total_paragraphs = len(paragraphs)
        print(f'TOTAL DE PARAGRAFOS: {total_paragraphs}')


        while True:
            end_paragraph = min(self.start_paragraph + self.paragraphs_per_page, total_paragraphs)
        
            print(f"\nVisualizando parágrafos {self.start_paragraph + 1} a {end_paragraph} de {total_paragraphs}\n")
            for i in range(self.start_paragraph, end_paragraph):
                print(paragraphs[i])


            if end_paragraph >= total_paragraphs:
                print("Você chegou ao final do documento.")
                input("Pressione Enter para voltar aos detalhes do documento.")
                return DocumentDetailView(self.doc_controller, self.documento)

            print("1. Ver mais parágrafos")
            print("2. Voltar aos detalhes do documento")
            opcao = input("Opção: ")

            if opcao == '1':
                self.start_paragraph = end_paragraph
                if self.start_paragraph >= total_paragraphs:
                    print("Você já visualizou todos os parágrafos.")
                    input("Pressione Enter para voltar aos detalhes do documento.")
                    return DocumentDetailView(self.doc_controller, self.documento)
            elif opcao == '2':
                input("Pressione Enter para voltar aos detalhes do documento.")
                return DocumentDetailView(self.doc_controller, self.documento)
            else:
                print("Opção inválida.")