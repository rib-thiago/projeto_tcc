from pymongo import MongoClient

class MongoDBConfig:
    def __init__(self, uri):
        self.uri = uri
        self.db = None

    def connect(self):
        """ Estabelece a conexão com o MongoDB """
        try:
            self.client = MongoClient(self.uri)
            self.db = self.client.get_database('banco_de_teste')  # Use default database
            print("Conexão com MongoDB estabelecida!")
        except Exception as e:
            print(f"Erro ao conectar ao MongoDB: {e}")

    def get_database(self):
        """ Retorna o objeto de banco de dados MongoDB """
        return self.db

    def close_connection(self):
        """ Fecha a conexão com o MongoDB """
        if self.client:
            self.client.close()
            print("Conexão com MongoDB fechada.")

    def get_collection(self, collection_name):
        """ Retorna a coleção específica do MongoDB """
        if self.db is not None:  # Verificar se o banco de dados foi inicializado corretamente
            return self.db[collection_name]
        else:
            raise Exception("Conexão com MongoDB não foi estabelecida.")

# Exemplo de uso:
# config = MongoDBConfig(host='localhost', port=27017)
# config.connect()
# db = config.get_database()
# documents_collection = db['documents']
# paragraphs_collection = db['paragraphs']
