import unittest
from projeto.utils.validators import ParagraphValidator
from projeto.models.paragraph import Paragraph  # Importe o modelo de parágrafo que você está usando

class TestParagraphValidator(unittest.TestCase):
    
    def setUp(self):
        # Configuração inicial, se necessário
        pass
    
    def test_validate_content_required(self):
        all_paragraphs = [
            Paragraph(num_paragraph=1, content="First paragraph", document_id="123"),
            Paragraph(num_paragraph=3, content="Third paragraph", document_id="123")
        ]       
        
        paragraph = Paragraph(num_paragraph=4, content="", document_id="123")
        errors = ParagraphValidator.validate(paragraph, all_paragraphs)
        print(f"Validation errors: {errors}")
        self.assertIn("Content is required.", errors)
    
    def test_validate_num_paragraph_required(self):
        all_paragraphs = [
            Paragraph(num_paragraph=1, content="First paragraph", document_id="123"),
            Paragraph(num_paragraph=3, content="Third paragraph", document_id="123")
        ]
        paragraph = Paragraph(num_paragraph=None, content="Lorem ipsum", document_id="123")
        errors = ParagraphValidator.validate(paragraph, all_paragraphs)
        print(f"Validation errors: {errors}")
        self.assertIn("Paragraph number is required.", errors)
    
    def test_validate_document_id_required(self):
        paragraph = Paragraph(num_paragraph=1, content="Lorem ipsum", document_id=None)
        errors = ParagraphValidator.validate(paragraph, [])
        print(f"Validation errors: {errors}")
        self.assertIn("Document ID is required.", errors)
    
    def test_validate_document_id_exists(self):
       all_paragraphs = [
           Paragraph(num_paragraph=1, content="Lorem ipsum", document_id="123"),
           Paragraph(num_paragraph=2, content="Dolor sit amet", document_id="456")
       ]
       paragraph = Paragraph(num_paragraph=3, content="Consectetur adipiscing elit", document_id="789")
       errors = ParagraphValidator.validate(paragraph, all_paragraphs)
       print(f"Validation errors: {errors}")
       self.assertIn("Não existe um documento com este _id.", errors)
    
    def test_validate_unique_paragraph_number(self):
        all_paragraphs = [
            Paragraph(num_paragraph=1, content="Lorem ipsum", document_id="123"),
            Paragraph(num_paragraph=2, content="Dolor sit amet", document_id="123")
        ]
        paragraph = Paragraph(num_paragraph=2, content="Duplicated paragraph number", document_id="123")
        errors = ParagraphValidator.validate(paragraph, all_paragraphs)
        print(f"Validation errors: {errors}")
        self.assertIn("Número de parágrafo duplicado para este documento.", errors)
    
    
    def tearDown(self):
        # Limpeza após os testes, se necessário
        pass

if __name__ == "__main__":
    unittest.main()

