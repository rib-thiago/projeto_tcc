# Projeto de Gerenciamento de Documentos

## Visão Geral

Aplicação de linha de comando (CLI) desenvolvida em Python para gerenciamento de documentos. 

Permite inserir, listar, atualizar e deletar documentos armazenados em um banco de dados MongoDB. 

O objetivo é oferecer uma ferramenta simples e eficiente para gerenciar documentos, facilitando operações como tradução, segmentação de parágrafos e extração de metadados.

## Funcionalidades

- Inserir novos documentos
- Listar documentos cadastrados
- Atualizar documentos existentes
- Deletar documentos com confirmação
- Conectar-se a um banco de dados MongoDB para armazenar e recuperar documentos


## Estrutura de Diretórios


```
project/
├── models/
│   ├── document.py        # Classe Document
│   ├── paragraph.py       # Classe Paragraph
├── views/
│   ├── tui.py             # Interface de Usuário Textual (TUI)
│   ├── document_view.py   # Visão de Documento
├── controllers/
│   ├── document_controller.py  # Controlador de Documentos
│   ├── paragraph_controller.py # Controlador de Parágrafos
├── services/
│   ├── document_service.py     # Serviço de Documentos
│   ├── translation_service.py  # Serviço de Tradução
├── persistence/
│   ├── mongodb/
│       ├── mongodb_config.py            # Configuração do MongoDB
│       ├── document_repository_impl.py  # Implementação do Repositório de Documentos
│       ├── paragraph_repository_impl.py # Implementação do Repositório de Parágrafos
├── utils/
│   ├── file_handlers.py   # Manipuladores de Arquivos
│   ├── text_utils.py      # Utilitários de Texto
└── main.py                 # Ponto de Entrada da Aplicação
``` 

**controllers/**: Contém os controladores da aplicação, responsáveis por intermediar a interação entre a interface do usuário e os serviços.

**models/**: Define os modelos de dados da aplicação, como a classe Document.

**persistence/**: Responsável por toda a lógica de persistência de dados. Inclui subdiretórios para diferentes tipos de persistência, como **mongodb/** para MongoDB.

**services/**: Implementa a lógica de negócios da aplicação, servindo como uma camada intermediária entre os controladores e os repositórios.

**views/**: Contém a interface de usuário, implementada inicialmente como TUI (Text User Interface).

**main.py**: Ponto de entrada da aplicação, responsável por iniciar e configurar os componentes principais do sistema.


## Padrões Utilizados

**MVC (Model-View-Controller)**: O projeto segue o padrão arquitetural MVC para separar a lógica de negócios da apresentação e manipulação de dados:

- **Model**: Representado pelas classes em **models/**, como Document, que encapsulam os dados e a lógica relacionada a eles.

- **View**: Implementado inicialmente em views/tui.py, utilizando uma interface de usuário baseada em texto para interação com o usuário.

- **Controller**: Implementado em controllers/, que coordena a lógica de aplicação e a entrada do usuário, chamando serviços para processamento.

**Repository Pattern**: O padrão Repository é adotado na camada de persistência (persistence/), onde cada repositório (DocumentRepository, por exemplo) isola a lógica de acesso aos dados da aplicação, ocultando os detalhes de como os dados são armazenados e recuperados.

**Relacionamento entre Camadas**: 

- **Controllers → Services**: Os controladores da aplicação interagem diretamente com os serviços para solicitar operações de negócio específicas, como inserir, atualizar ou deletar um documento.

- **Services → Repositories**: Os serviços utilizam os repositórios para acessar e manipular os dados persistidos. Eles encapsulam a lógica de negócios e coordenam as operações entre os controladores e os repositórios.

## Dependências

- Python 3.10.13
- pymongo para integração com o MongoDB.
