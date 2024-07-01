from projeto.persistence.mongodb.mongodb_config import MongoDBConfig
from projeto.models.document import Document
from bson import ObjectId

class DocumentRepository:
    def __init__(self, mongo_config):
        self.mongo_config = mongo_config
        self.collection = self.mongo_config.get_collection('documents')

    def insert_document(self, document):
        """ Insere um novo documento no MongoDB """
        doc_dict = document.to_dict()
        result = self.collection.insert_one(doc_dict)
        return result.inserted_id

    def list_documents(self):
        documents = self.collection.find()
        return [Document(doc['title'], doc['author'], doc['language'], doc['_id']) for doc in documents]

    def update_document(self, document_id, field, new_value):
        """ Atualiza um campo específico de um documento no MongoDB """
        update_result = self.collection.update_one(
            {'_id': ObjectId(document_id)},
            {'$set': {field: new_value}}
        )
        return update_result.modified_count

    def delete_document(self, document_id):
        """ Deleta um documento do MongoDB """
        result = self.collection.delete_one({'_id': ObjectId(document_id)})
        return result.deleted_count

    def get_document_by_id(self, document_id):
        doc = self.collection.find_one({'_id': ObjectId(document_id)})
        if doc:
            return Document(doc['title'], doc['author'], doc['language'], doc['_id'])
        else:
            return None