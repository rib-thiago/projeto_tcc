from projeto.persistence.mongodb.mongodb_config import MongoDBConfig
from projeto.models.paragraph import Paragraph

class ParagraphRepository:
    def __init__(self):
        self.mongo_config = MongoDBConfig()
        self.mongo_config.connect()
        self.collection = self.mongo_config.get_collection('paragraphs')

    def translate_paragraph(self, paragraph_id, translation_data):
        """ Realiza a tradução de um parágrafo e salva no MongoDB """
        result = self.collection.update_one({'_id': paragraph_id}, {'$set': translation_data})
        return result.modified_count

    def list_paragraphs_to_translate(self, document_id):
        """ Lista os parágrafos de um documento que ainda não foram traduzidos """
        paragraphs = list(self.collection.find({'document_id': document_id, 'translated_content': None}))
        return [Paragraph.from_dict(para) for para in paragraphs]
