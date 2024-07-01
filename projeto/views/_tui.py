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
        filepath = input("Path do Arquivo de Documento: ")
        source = input("Url da fonte do Documento, se aplicável: ")
        success, message = self.doc_controller.insert_document(title, author, language, filepath, source)

        if success:
            print(f'\n{message}')
        else:
            print(f"Erro ao inserir documento: {message}")


    def listar_documentos(self):
        documentos = self.doc_controller.list_documents()
        print("\nDocumentos Cadastrados:\n")
        for idx, documento in enumerate(documentos):
            print(f'{idx + 1}. {documento.title} - {documento.author}\n')

        escolha = input("\nDigite o número do documento para visualizar mais detalhes ou 'v' para voltar ao menu principal: ")
        
        if escolha.lower() == 'v':
            return
        else:
            try:
                escolha_idx = int(escolha) - 1
                if 0 <= escolha_idx < len(documentos):
                    self.visualizar_documento(documentos[escolha_idx])
                else:
                    print("Opção inválida.")
            except ValueError:
                print("Entrada inválida.")

    def visualizar_documento(self, documento):
        print("\nDetalhes do Documento:\n")
        print(documento)
        
        print("\nEscolha uma opção:\n")
        print("1. Visualizar Texto do Documento")
        print("2. Atualizar Documento")
        print("3. Deletar Documento")
        print("4. Voltar ao Menu Principal\n")
        opcao = input("Opção: ")

        if opcao == '1':
            print(f'Conteúdo:\n\n{documento.text}')
        elif opcao == '2':
            self.atualizar_documento(documento._id)
        elif opcao == '3':
            self.deletar_documento(documento._id)
        elif opcao == '4':
            return
        else:
            print("Opção inválida. Retornando ao menu principal.")

    def atualizar_documento(self, document_id):
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

    def deletar_documento(self, document_id):
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