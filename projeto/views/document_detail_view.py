from projeto.views.base_view import BaseView

class DocumentDetailView(BaseView):
    def __init__(self, view_manager, documento):
        super().__init__(view_manager)
        self.documento = documento

    def display(self):
        # Exibe os detalhes do documento em uma tabela simples
        print("\nDetalhes do Documento:\n")
        print(f"Título: {self.documento.title}")
        print(f"Autor: {self.documento.author}")
        print(f"Idioma: {self.documento.language}")
        print(f"Filepath: {self.documento.filepath}")
        print(f"Source: {self.documento.source}")
        print(f"Número de Parágrafos: {self.documento.num_paragraphs}")
        # print(f"Número de Páginas: {self.documento.num_pages}")
        print(f"Data de Criação: {self.documento.created_at.strftime('%d/%m/%Y')}")

        # Exibe as opções de navegação
        print("\nEscolha uma opção:")
        print("[1] Visualizar Texto do Documento")
        print("[2] Visualizar Parágrafos do Documento")
        print("[3] Atualizar Dados do Documento")
        print("[4] Deletar Documento")
        print("[5] Voltar ao Menu Principal")

        opcao = input("> ")

        # Lógica para lidar com a opção escolhida
        if opcao == '1':
            return self.view_manager.get_view('DocumentContentView', self.documento)
        elif opcao == '2':
            return self.view_manager.get_view('DocumentParagraphListView', self.documento)
        elif opcao == '3':
            return self.view_manager.get_view('DocumentUpdateView', self.documento)
        elif opcao == '4':
            return self.view_manager.get_view('DocumentDeleteView', self.documento)
        elif opcao == '5':
            print("\nPressione Enter para voltar à lista de documentos...")
            input("")
            return self.view_manager.get_view('MainMenuView')
        else:
            print("\nOpção inválida, pressione enter para retornar ao menu")
            input("")
            return self.view_manager.get_view('MainMenuView')
