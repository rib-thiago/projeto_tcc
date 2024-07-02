from projeto.persistence.mongodb.mongodb_config import MongoDBConfig
from projeto.models.paragraph import Paragraph
from bson import ObjectId

class ParagraphRepository:
    def __init__(self, mongo_config):
        self.mongo_config = mongo_config
        self.collection = self.mongo_config.get_collection('paragraphs')

    def insert_paragraph(self, paragraph):
        """ Insere um novo documento no MongoDB """
        para_dict = paragraph.to_dict()
        result = self.collection.insert_one(para_dict)
        return result.inserted_id

    def count_paragraphs_by_doc_id(self, doc_id):
        """ Conta o número de parágrafos com um determinado doc_id """
        return self.collection.count_documents({'document_id': ObjectId(doc_id)})

    def list_paragraphs_by_doc_id(self, doc_id):
        """ Lista todos os parágrafos com um determinado doc_id """
        return list(self.collection.find({'document_id': ObjectId(doc_id)}))
