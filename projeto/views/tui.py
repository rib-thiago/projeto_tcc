from projeto.controllers.document_controller import DocumentController

class TUI:
    def __init__(self, mongo_config):
        self.doc_controller = DocumentController(mongo_config)
        self.mongo_config = mongo_config


    def mostrar_menu(self):
        print("\n=== Menu ===")
        print("1. Inserir Documento")
        print("2. Listar Documentos")
        print("3. Sair")

    def executar(self):
        while True:
            self.mostrar_menu()
            escolha = input("Escolha uma opção: ")

            if escolha == '1':
                self.insert_document()
            elif escolha == '2':
                self.listar_documentos()
            elif escolha == '3':
                print("Saindo...")
                break
            else:
                print("Opção inválida!")

    def insert_document(self):
        print("\nInserir Novo Documento\n")
        title = input("Título do Documento: ")
        author = input("Autor do Documento: ")
        language = input("Idioma do Documento: ")
        
        success, message = self.doc_controller.insert_document(title, author,language)
        if success:
            print(f'\n{message}')
        else:
            print(f"Erro ao inserir documento: {message}")

    def listar_documentos(self):
        documentos = self.doc_controller.list_documents()
        print("\nDocumentos Cadastrados:\n")
        for documento in documentos:
            print(f'{documento}\n')
        
        print("\nEscolha uma opção:\n")
        print("1. Atualizar Documento")
        print("2. Deletar Documento")
        print("3. Voltar ao Menu Principal\n")
        opcao = input("Opção: ")
        
        if opcao == '1':
            self.atualizar_documento()
        elif opcao == '2':
            self.deletar_documento()
        elif opcao == '3':
            return
        else:
            print("Opção inválida. Retornando ao menu principal.")
    
    def atualizar_documento(self):
        document_id = input("\nInforme o ID do documento a ser atualizado: ")
        documento = self.doc_controller.get_document_by_id(document_id)
        
        if documento:
            print(f"\nDocumento encontrado:\n\n{documento}\n")
            field = input("\nInforme o campo a ser atualizado (ex. title, author, language): ")
            new_value = input(f"\nInforme o novo valor para o campo {field}: ")
            success, message = self.doc_controller.update_document(document_id, field, new_value)
            if success:
                print("\nDocumento atualizado com sucesso:\n")
                documento = self.doc_controller.get_document_by_id(document_id)
                print(f'{documento}\n')
            else:
                print(f"Erro: {message}")
        else:
            print("Documento não encontrado.")
    
    def deletar_documento(self):
        document_id = input("\nInforme o ID do documento a ser deletado: ")
        documento = self.doc_controller.get_document_by_id(document_id)
        
        if documento:
            print(f"\nDocumento encontrado:\n\n{documento}\n")
            confirmacao = input("\nTem certeza que deseja deletar este documento? (s/n): ")
            if confirmacao.lower() == 's':
                success, message = self.doc_controller.delete_document(document_id)
                if success:
                    print("\nDocumento deletado com sucesso.\n")
                else:
                    print(f"Erro: {message}")
            else:
                print("Exclusão cancelada.")
        else:
            print("Documento não encontrado.")
