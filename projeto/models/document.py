from datetime import datetime
from bson import ObjectId

class Document:
    def __init__(self, title, author, language, _id=None):
        self.title = title
        self.author = author
        self.language = language
        self._id = _id if _id else ObjectId()

    def __str__(self):
        return f"Id: {self._id}\nTitulo: {self.title}\nAutor: {self.author}\nIdioma: {self.language}"

    def to_dict(self):
        return {
            '_id': self._id,
            'title': self.title,
            'author': self.author,
            'language': self.language,
        }

    @classmethod
    def from_dict(cls, doc_dict):
        return cls(
            title=doc_dict['title'],
            author=doc_dict['author'],
            language=doc_dict['language'],
            _id=doc_dict.get('_id')
        )

#filepath,
#source, 
#num_paragraphs, num_pages=None, datetime=None



#'filepath': self.filepath,
#'source': self.source,
#'num_paragraphs': self.num_paragraphs,
#'num_pages': self.num_pages,
#'datetime': self.datetime


#            filepath=doc_dict['filepath'],
#            source=doc_dict['source'],
#            num_paragraphs=doc_dict['num_paragraphs'],
#            num_pages=doc_dict.get('num_pages'),
#            datetime=doc_dict['datetime']


