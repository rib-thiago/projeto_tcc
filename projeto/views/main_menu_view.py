from projeto.views.document_insert_view import DocumentInsertView
from projeto.views.document_list_view import DocumentListView

class MainMenuView:
    def __init__(self, doc_controller):
        self.doc_controller = doc_controller

    def display(self):
        print("\n=== Menu ===")
        print("1. Inserir Documento")
        print("2. Listar Documentos")
        print("3. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            return DocumentInsertView(self.doc_controller)
        elif escolha == '2':
            return DocumentListView(self.doc_controller)
        elif escolha == '3':
            print("Saindo...")
            return None
        else:
            print("Opção inválida!")
            return self
