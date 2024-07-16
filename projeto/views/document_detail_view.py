from projeto.views.base_view import BaseView

class DocumentDetailView(BaseView):
    def __init__(self, view_manager, document_id):
        super().__init__(view_manager)
        self.document_id = document_id
        

    def display(self):
        self.document = self.get_doc_controller().get_document_by_id(self.document_id)
        
        if not self.document:
            print("Documento não encontrado.")
            return self.view_manager.get_view('MainMenuView')

        # Atualiza o número de parágrafos do documento
        self.update_num_paragraphs()

        self.print_document_info()
        print('\n')
        self.print_navigation_options()

        opcao = input("> ")

        # Lógica para lidar com a opção escolhida
        if opcao == '1':
            return self.view_manager.get_view('DocumentContentView', self.document)
        elif opcao == '2':
            return self.view_manager.get_view('DocumentParagraphListView', self.document)
        elif opcao == '3':
            return self.view_manager.get_view('DocumentUpdateView', self.document)
        elif opcao == '4':
            return self.view_manager.get_view('DocumentDeleteView', self.document)
        elif opcao == '5':
            print("\nPressione Enter para voltar à lista de documentos...")
            input("")
            return self.view_manager.get_view('MainMenuView')
        else:
            print("\nOpção inválida, pressione enter para retornar ao menu")
            input("")
            return self.view_manager.get_view('MainMenuView')

    def print_document_info(self):
            # Exibe as informações atuais do documento
            print("\nDetalhes do Documento:\n")
            print(f"Título: {self.document.title}")
            print(f"Autor: {self.document.author}")
            print(f"Idioma: {self.document.language}")
            print(f"Fonte: {self.document.source}")
            print(f"Número de Parágrafos: {self.document.num_paragraphs}")
            print(f"Data de Criação: {self.document.created_at.strftime('%d/%m/%Y')}")

    def print_navigation_options(self):
        """ Exibe as opções de navegação """
        print("\nEscolha uma opção:")
        print("[1] Visualizar Texto do Documento")
        print("[2] Visualizar Parágrafos do Documento")
        print("[3] Atualizar Dados do Documento")
        print("[4] Deletar Documento")
        print("[5] Voltar ao Menu Principal")

    def update_num_paragraphs(self):
        # Atualiza o número de parágrafos do documento
        self.document.num_paragraphs = self.get_para_controller().count_paragraphs_by_doc_id(self.document_id)[0]