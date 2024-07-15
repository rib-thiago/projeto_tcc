from projeto.views.base_view import BaseView

class MainMenuView(BaseView):
    def display(self):
        # Exibe o menu principal
        print(f'=== Menu Principal ===')
        print("\n")
        print("[1] Inserir Documento")
        print("[2] Listar Documentos")
        print("[3] Sair")

        # Recebe a escolha do usuário
        escolha = input("> ")

        # Lógica para lidar com a escolha do usuário
        if escolha == '1':
            return self.view_manager.get_view('DocumentInsertView')
        elif escolha == '2':
            return self.view_manager.get_view('DocumentListView')
        elif escolha == '3':
            print('Saindo...')
            return None
        else:
            print('Opção inválida! Pressione Enter para retornar ao Menu')
            input("")
            return self
