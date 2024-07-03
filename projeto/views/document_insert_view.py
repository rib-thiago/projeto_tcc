from rich.console import Console
from rich.panel import Panel
from projeto.views.base_view import BaseView

class DocumentInsertView(BaseView):
    def display(self):
        console = Console()
        console.print(Panel("Inserir Novo Documento\n", title="Novo Documento", style="green on black", width=100))

        console.print(Panel(f'Título do Documento: ', style="green on black", width=100))
        title = input("")
        console.print(Panel(f'Autor do Documento: ', style="green on black", width=100))
        author = input("")
        console.print(Panel(f'Idioma do Documento: ', style="green on black", width=100))
        language = input("")
        console.print(Panel(f'Path do Arquivo de Documento: ', style="green on black", width=100))
        filepath = input("")
        console.print(Panel(f'URL da fonte do Documento, se aplicável: ', style="green on black", width=100))
        source = input("")

        success, message = self.get_doc_controller().insert_document(title, author, language, filepath, source)

        if success:
            console.print(Panel(f'\n{message}', style="green on black", width=100))
        else:
            console.print(Panel(f"Erro ao inserir documento: {message}", style="red on black", width=100))

        console.print(Panel("Pressione Enter para voltar ao menu principal...", style="green on black", width=100))
        input("")
        return self.view_manager.get_view('MainMenuView')
