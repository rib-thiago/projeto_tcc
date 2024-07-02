from projeto.views.base_view import BaseView


class DocumentDetailView(BaseView):
    def __init__(self, view_manager, documento):
        super().__init__(view_manager)
        self.documento = documento

    def display(self):
        print("\nDetalhes do Documento:\n")
        print(self.documento)
        
        print("\nEscolha uma opção:\n")
        print("1. Visualizar Texto do Documento")
        print("2. Atualizar Documento")
        print("3. Deletar Documento")
        print("4. Voltar ao Menu Principal\n")
        opcao = input("Opção: ")

        if opcao == '1':
            return self.view_manager.get_view('DocumentContentView', self.documento)
        elif opcao == '2':
            return self.view_manager.get_view('DocumentUpdateView', self.documento)
        elif opcao == '3':
            return self.view_manager.get_view('DocumentDeleteView', self.documento)
        elif opcao == '4':
            input("Pressione Enter para voltar ao menu principal...")
            return self.view_manager.get_view('MainMenuView') 

        else:
            print("Opção inválida. Retornando ao menu principal.")
            return self.view_manager.get_view('MainMenuView')

