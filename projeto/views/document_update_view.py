from projeto.views.base_view import BaseView

class DocumentUpdateView(BaseView):
    def __init__(self, view_manager, document):
        super().__init__(view_manager)
        self.document = document

    def display(self):
        while True:
            self.print_document_info()

            fields_and_values = self.field_selector()

            for field, new_value in fields_and_values:
                success, message = self.get_doc_controller().update_document(self.document._id, field, new_value)

                if success:
                    print(f"\nCampo '{field}' atualizado com sucesso para '{new_value}'.")
                else:
                    print(f"\nErro ao atualizar campo '{field}': {message}")
                    input("\nPressione Enter para tentar novamente...")
                    return self.view_manager.get_view('DocumentDetailView', self.document)

            print("\nDocumento atualizado com sucesso.")
            print("\nPressione Enter para voltar aos detalhes do documento...")
            input("")
            return self.view_manager.get_view('DocumentDetailView', self.document._id)

    def print_document_info(self):
            # Exibe as informações atuais do documento
            print("\nAtualizar Documento:\n")
            print(f"Título: {self.document.title}")
            print(f"Autor: {self.document.author}")
            print(f"Idioma: {self.document.language}")
            # print(f"Filepath: {self.document.filepath}")
            print(f"Fonte: {self.document.source}")
            print(f"Número de Parágrafos: {self.document.num_paragraphs}")
            print(f"Data de Criação: {self.document.created_at.strftime('%d/%m/%Y')}")

    def field_selector(self):
        """ Filtra os parágrafos com base nas preferências do usuário """
        field_mapping = {
            '1': 'title',
            '2': 'author',
            '3': 'language',
            '4': 'source'
        }

        print("Escolha os campos a serem editados:")
        print("[1] Titulo")
        print("[2] Autor")
        print("[3] Idioma")
        print("[4] Fonte\n")

        print("Digite o número dos campos separados por vírgula: \n")
        option_input = input("> ")
        options = option_input.split(',')

        field_value_pairs = []

        for option in options:
            field = field_mapping.get(option.strip())
            if field:
                print(f"\nInforme o novo valor para o campo {field}: ")
                new_value = input("> ")
                field_value_pairs.append((field, new_value))
            else:
                print(f"Opção inválida: {option.strip()}.")

        return field_value_pairs








