Para lidar com a validação da numeração de parágrafos e futuras atualizações caso haja necessidade de renumeração devido a problemas como divisões incorretas ou captura de ruído pelo OCR, você pode seguir algumas estratégias:

Validação inicial de números de parágrafos: Implemente uma validação que verifique se o número do parágrafo a ser inserido não está duplicado com números já existentes no documento. Isso pode ser feito de forma semelhante à validação do título do documento, verificando se já existe um parágrafo com o mesmo número para o mesmo documento.

Atualização automática ou manual de números de parágrafos: Caso seja necessário renumerar parágrafos devido a alterações na estrutura do texto (como correções feitas manualmente), você precisará de um mecanismo para atualizar esses números. Isso pode ser feito através de um processo automatizado que renumera todos os parágrafos de um documento com base na ordem atual, ou manualmente através de uma interface que permita editar os números dos parágrafos.

Validação contínua e ajustes: Implemente rotinas de validação contínua sempre que houver alterações nos parágrafos ou no documento. Por exemplo, ao adicionar um novo parágrafo, verifique se a numeração continua consistente e se não há números duplicados. Se houver necessidade de renumeração, isso pode ser desencadeado automaticamente ou após uma intervenção manual.

Histórico de versões: Considere manter um histórico de versões dos documentos que registre as mudanças nos parágrafos ao longo do tempo. Isso pode facilitar o rastreamento de quando e por que ocorreram mudanças na numeração dos parágrafos.





validação de ordenação!

    @staticmethod
    def validate_ordered_paragraph_numbers(paragraph, all_paragraphs):
        errors = []
        if all_paragraphs is not None:
            document_paragraphs = [p for p in all_paragraphs if p.document_id == paragraph.document_id]
            if document_paragraphs:
                sorted_paragraphs = sorted(document_paragraphs, key=lambda p: p.num_paragraph)
                expected_paragraph_number = 1
                for p in sorted_paragraphs:
                    if paragraph.num_paragraph < expected_paragraph_number:
                        errors.append("Número de parágrafo fora de ordem.")
                        break
                    expected_paragraph_number += 1
                if paragraph.num_paragraph != expected_paragraph_number:
                    errors.append("Número de parágrafo fora de ordem.")
        return errors



    def test_validate_ordered_paragraph_numbers(self):
        all_paragraphs = [
            Paragraph(num_paragraph=1, content="First paragraph", document_id="123"),
            Paragraph(num_paragraph=3, content="Third paragraph", document_id="123")
        ]
        
        paragraph = Paragraph(num_paragraph=2, content="Second paragraph", document_id="123")
        print(f"All paragraphs: {[p.num_paragraph for p in all_paragraphs]}")
        print(f"Current paragraph num: {paragraph.num_paragraph}")
        errors = ParagraphValidator.validate(paragraph, all_paragraphs)
        print(f"Validation errors: {errors}")
        self.assertIn("Número de parágrafo fora de ordem.", errors)

        # Test case where inserting a paragraph with num_paragraph = 2 should be valid
        paragraph = Paragraph(num_paragraph=2, content="Second paragraph", document_id="123")
        print(f"All paragraphs: {[p.num_paragraph for p in all_paragraphs]}")
        print(f"Current paragraph num: {paragraph.num_paragraph}")
        errors = ParagraphValidator.validate(paragraph, all_paragraphs)
        print(f"Validation errors: {errors}")
        self.assertEqual(len(errors), 1)

        # Test case where inserting a paragraph with num_paragraph = 4 should fail
        paragraph = Paragraph(num_paragraph=4, content="Fourth paragraph", document_id="123")
        print(f"All paragraphs: {[p.num_paragraph for p in all_paragraphs]}")
        print(f"Current paragraph num: {paragraph.num_paragraph}")
        errors = ParagraphValidator.validate(paragraph, all_paragraphs)
        print(f"Validation errors: {errors}")
        self.assertIn("Número de parágrafo fora de ordem.", errors)

        # Test case where inserting a paragraph with num_paragraph = 1 should fail
        paragraph = Paragraph(num_paragraph=1, content="Another first paragraph", document_id="123")
        print(f"All paragraphs: {[p.num_paragraph for p in all_paragraphs]}")
        print(f"Current paragraph num: {paragraph.num_paragraph}")
        errors = ParagraphValidator.validate(paragraph, all_paragraphs)
        print(f"Validation errors: {errors}")
        self.assertIn("Número de parágrafo fora de ordem.", errors)

        # Test case where inserting a paragraph with num_paragraph = 5 should be valid
        paragraph = Paragraph(num_paragraph=5, content="Fifth paragraph", document_id="123")
        print(f"All paragraphs: {[p.num_paragraph for p in all_paragraphs]}")
        print(f"Current paragraph num: {paragraph.num_paragraph}")
        errors = ParagraphValidator.validate(paragraph, all_paragraphs)
        print(f"Validation errors: {errors}")
        self.assertEqual(len(errors), 1)
