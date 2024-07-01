class DocumentDeleteView:
    def __init__(self, doc_controller, documento):
        self.doc_controller = doc_controller
        self.documento = documento

    def display(self):
        from projeto.views.main_menu_view import MainMenuView
        confirmacao = input("\nTem certeza que deseja deletar este documento? (s/n): ")
        if confirmacao.lower() == 's':
            success, message = self.doc_controller.delete_document(self.documento._id)
            if success:
                print("\nDocumento deletado com sucesso.\n")
            else:
                print(f"Erro: {message}")
        else:
            print("Exclusão cancelada.")

        input("Pressione Enter para voltar ao menu principal...")
        return MainMenuView(self.doc_controller)