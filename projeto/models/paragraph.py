class Paragraph:
    def __init__(self, document_id, content, translated_content=None, translated_by=None, translation_engine=None,
                source_language=None, target_language=None):
        self.document_id = document_id
        self.content = content
        self.translated_content = translated_content
        self.translated_by = translated_by
        self.translation_engine = translation_engine
        self.source_language = source_language
        self.target_language = target_language

    def to_dict(self):
        """ Converte o objeto Paragraph para um dicionário """
        return {
            'document_id': self.document_id,
            'content': self.content,
            'translated_content': self.translated_content,
            'translated_by': self.translated_by,
            'translation_engine': self.translation_engine,
            'source_language': self.source_language,
            'target_language': self.target_language
        }

    @classmethod
    def from_dict(cls, para_dict):
        """ Cria um objeto Paragraph a partir de um dicionário """
        return cls(
            document_id=para_dict['document_id'],
            content=para_dict['content'],
            translated_content=para_dict.get('translated_content'),
            translated_by=para_dict.get('translated_by'),
            translation_engine=para_dict.get('translation_engine'),
            source_language=para_dict.get('source_language'),
            target_language=para_dict.get('target_language')
        )
