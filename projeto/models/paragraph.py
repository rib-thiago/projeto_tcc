from bson import ObjectId

class Paragraph:
    def __init__(self, num_paragraph, content, document_id, translated_content=None, _id=None):
        self._id = _id if _id else ObjectId()
        self.document_id = document_id
        self.content = content
        self.num_paragraph= num_paragraph
        self.translated_content = translated_content
        self.translated = False

    def to_dict(self):
        """ Converte o objeto Paragraph para um dicionário """
        return {
            '_id': self._id,
            'document_id': self.document_id,
            'content': self.content,
            'num_paragraph': self.num_paragraph,
            'translated_content': self.translated_content,
            'translated': self.translated
        }

    @classmethod
    def from_dict(cls, para_dict):
        """ Cria um objeto Paragraph a partir de um dicionário """
        return cls(
            document_id=para_dict['document_id'],
            content=para_dict['content'],
            num_paragraph=para_dict.get['num_paragraph'],
            _id=para_dict.get('_id'),
            translated_content=para_dict.get('translated_content'),
            translated=para_dict.get('translated')
        )

