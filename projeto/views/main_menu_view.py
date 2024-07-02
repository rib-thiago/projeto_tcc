from projeto.views.base_view import BaseView

class MainMenuView(BaseView):
    def display(self):
        print("\n=== Menu ===")
        print("1. Inserir Documento")
        print("2. Listar Documentos")
        print("3. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            return self.view_manager.get_view('DocumentInsertView')
        elif escolha == '2':
            return self.view_manager.get_view('DocumentListView')
        elif escolha == '3':
            print("Saindo...")
            return None
        else:
            print("Opção inválida!")
            return self
