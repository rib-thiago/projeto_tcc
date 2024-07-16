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
        """ Conta o número de parágrafos com um determinado doc_id e quantos estão traduzidos """
        total_paragraphs = self.collection.count_documents({'document_id': ObjectId(doc_id)})
        translated_paragraphs = self.collection.count_documents({'document_id': ObjectId(doc_id), 'translated': True})
        return total_paragraphs, translated_paragraphs

    def list_paragraphs_by_doc_id(self, doc_id):
        """Lista todos os parágrafos com um determinado doc_id"""
        paragraphs = self.collection.find({'document_id': ObjectId(doc_id)})
        # Cria uma lista de objetos Paragraph
        paragraph_list = [Paragraph.from_dict(paragraph) for paragraph in paragraphs]
        return paragraph_list
    
    def get_paragraph_content(self, document_id, num_paragraph):
        try:
            paragraph = self.collection.find_one({"document_id": ObjectId(document_id), "num_paragraph": int(num_paragraph)})
            if paragraph:
                return paragraph['content']
            else:
                print(f"Parágrafo não encontrado para document_id={document_id} e num_paragraph={num_paragraph}")
                return None
        except Exception as e:
            print(f"Erro ao buscar parágrafo: {e}")
            return None

    def update_paragraph_translation(self, document_id, num_paragraph, translation):
        try:
            result = self.collection.update_one(
                {"document_id": ObjectId(document_id), "num_paragraph": int(num_paragraph)},
                {"$set": {"translated_content": translation, "translated": True}}
            )
            if result.modified_count == 0:
                print(f"Nenhum documento foi atualizado para document_id={document_id} e num_paragraph={num_paragraph}")
            else:
                print(f"Documento atualizado com sucesso para document_id={document_id} e num_paragraph={num_paragraph}")
        except Exception as e:
            print(f"Erro ao atualizar parágrafo: {e}")

    def get_paragraph_translated(self, document_id, num_paragraph):
        try:
            paragraph = self.collection.find_one({"document_id": ObjectId(document_id), "num_paragraph": int(num_paragraph)})
            if paragraph['translated'] == True:
                return paragraph['translated'], paragraph['translated_content']
            else:
                return paragraph['translated'], ""
        except Exception as e:
            print(f"Erro ao buscar parágrafo: {e}")
            return None
        
    def delete_paragraphs_by_doc_id(self, doc_id):
        """ Deleta todos os parágrafos com um determinado doc_id """
        result = self.collection.delete_many({'document_id': ObjectId(doc_id)})
        return result.deleted_count