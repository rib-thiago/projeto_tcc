from datetime import datetime
from bson import ObjectId

class Document:
    def __init__(self, title, author, language, filepath, source, text, num_paragraphs=None, num_pages=None, created_at=None, _id=None):
        self.title = title
        self.author = author
        self.language = language
        self.filepath = filepath
        self.source = source
        self.num_paragraphs = num_paragraphs
        self.num_pages = num_pages
        self.created_at = created_at if created_at is not None else datetime.now()
        self._id = _id if _id else ObjectId()
        self.text = text  # Para armazenar o texto do documento


    def __str__(self):
        return f"Id: {self._id}\nTitulo: {self.title}\nAutor: {self.author}\nIdioma: {self.language}\nFilepath: {self.filepath}\nSource: {self.source}\nNum Paragraphs: {self.num_paragraphs}\nNum Pages: {self.num_pages}\nCreated At: {self.created_at}\n"

    def to_dict(self):
        return {
            '_id': self._id,
            'title': self.title,
            'author': self.author,
            'language': self.language,
            'filepath': self.filepath,
            'source': self.source,
            'num_paragraphs': self.num_paragraphs,
            'num_pages': self.num_pages,
            'created_at': self.created_at,
            'text': self.text
        }

    @classmethod
    def from_dict(cls, doc_dict):
        return cls(
            title=doc_dict['title'],
            author=doc_dict['author'],
            language=doc_dict['language'],
            filepath=doc_dict.get('filepath'),
            source=doc_dict.get('source'),
            num_paragraphs=doc_dict.get('num_paragraphs'),
            num_pages=doc_dict.get('num_pages'),
            created_at=doc_dict.get('created_at'),
            _id=doc_dict.get('_id'),
            text=doc_dict.get('text')
        )










