from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from projeto.views.base_view import BaseView

class MainMenuView(BaseView):
    def display(self):
        console = Console()

        # Constrói o painel com as opções do menu principal
        menu_text = Text()
        menu_text.append("\n")
        menu_text.append("[1] Inserir Documento", style="bold")
        menu_text.append("\n")
        menu_text.append("[2] Listar Documentos", style="bold")
        menu_text.append("\n")
        menu_text.append("[3] Sair", style="bold")

        console.print(Panel(menu_text, title="Menu Principal", style="green on black", width=100))

        # Recebe a escolha do usuário
        escolha = input("> ")

        # Lógica para lidar com a escolha do usuário
        if escolha == '1':
            return self.view_manager.get_view('DocumentInsertView')
        elif escolha == '2':
            return self.view_manager.get_view('DocumentListView')
        elif escolha == '3':
            console.print(Panel(f'Saindo...', style="green on black", width=100))
            return None
        else:
            console.print(Panel(f'Opção inválida! Pressione Enter para retornar ao Menu', style="red on black", width=100))
            input("")
            return self
