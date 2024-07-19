from bson import ObjectId

class ParagraphValidator:
    @staticmethod
    def validate_paragraphs(paragraphs):
        errors = []
        for paragraph in paragraphs:
            paragraph_errors = ParagraphValidator.validate(paragraph, paragraphs)
            if paragraph_errors:
                errors.append(paragraph_errors)
        return errors

    @staticmethod
    def validate(paragraph, all_paragraphs=None):
        errors = []
        if not paragraph.content:
            errors.append("Content is required.")
        if not paragraph.num_paragraph:
            errors.append("Paragraph number is required.")
        if not paragraph.document_id:
            errors.append("Document ID is required.")
        if paragraph.document_id:
            errors += ParagraphValidator.validate_document_id(paragraph.document_id, all_paragraphs)
        errors += ParagraphValidator.validate_unique_paragraph_number(paragraph.num_paragraph, paragraph.document_id, all_paragraphs)
        return errors

    @staticmethod
    def validate_document_id(document_id, all_paragraphs):
        errors = []
        if all_paragraphs is not None:
            document_ids = {p.document_id for p in all_paragraphs}
            if document_id not in document_ids:
                errors.append("Não existe um documento com este _id.")
        return errors

    @staticmethod
    def validate_unique_paragraph_number(paragraph_number, document_id, all_paragraphs):
        errors = []
        if all_paragraphs is not None:
            for p in all_paragraphs:
                if p.document_id == document_id and p.num_paragraph == paragraph_number:
                    errors.append("Número de parágrafo duplicado para este documento.")
        return errors


