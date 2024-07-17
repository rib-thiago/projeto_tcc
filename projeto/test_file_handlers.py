import unittest
import os
from unittest.mock import patch, mock_open
from projeto.utils.file_handlers import read_file, write_file, verify_file_path, split_pdf, pdf_to_images
from projeto.utils.exceptions import FileNotFoundError, IOError, PdfReadError, handle_exception

class TestFileHandlers(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="file content")
    def test_read_file_success(self, mock_file):
        result = read_file("test.txt")
        self.assertEqual(result, "file content")

    @patch("builtins.open", side_effect=FileNotFoundError("File not found"))
    def test_read_file_not_found(self, mock_file):
        with self.assertLogs(level='INFO') as log:
            read_file("test.txt")
            self.assertIn("File not found error occurred", log.output[0])

    @patch("builtins.open", side_effect=IOError("Error reading file"))
    def test_read_file_io_error(self, mock_file):
        with self.assertLogs(level='INFO') as log:
            read_file("test.txt")
            self.assertIn("I/O error occurred", log.output[0])

    @patch("builtins.open", new_callable=mock_open)
    def test_write_file_success(self, mock_file):
        write_file("test.txt", "content")
        mock_file().write.assert_called_once_with("content")

    @patch("builtins.open", side_effect=IOError("Error writing to file"))
    def test_write_file_io_error(self, mock_file):
        with self.assertLogs(level='INFO') as log:
            write_file("test.txt", "content")
            self.assertIn("I/O error occurred", log.output[0])

    def test_verify_file_path_success(self):
        with patch("os.path.abspath", return_value="test.txt"), \
             patch("os.path.isfile", return_value=True):
            result = verify_file_path("test.txt")
            self.assertEqual(result, 'txt')

    def test_verify_file_path_not_found(self):
        with patch("os.path.abspath", return_value="test.txt"), \
             patch("os.path.isfile", return_value=False), \
             self.assertLogs(level='INFO') as log:
            verify_file_path("test.txt")
            self.assertIn("File not found error occurred", log.output[0])

    def test_verify_file_path_unsupported_type(self):
        with patch("os.path.abspath", return_value="test.unsupported"), \
             patch("os.path.isfile", return_value=True), \
             self.assertLogs(level='INFO') as log:
            verify_file_path("test.unsupported")
            self.assertIn("An unexpected error occurred", log.output[0])

    def test_split_pdf_file_not_found(self):
        with patch("os.path.isfile", return_value=False), \
             self.assertLogs(level='INFO') as log:
            split_pdf("nonexistent.pdf", "output")
            self.assertIn("File not found error occurred", log.output[0])

    def test_pdf_to_images_io_error(self):
        with patch("os.path.exists", return_value=True), \
             patch("os.makedirs"), \
             patch("os.listdir", return_value=["test.pdf"]), \
             patch("file_handlers.convert_from_path", side_effect=IOError("Conversion error")), \
             self.assertLogs(level='INFO') as log:
            pdf_to_images("pdf_dir", "output_folder")
            self.assertIn("I/O error occurred", log.output[0])

if __name__ == "__main__":
    unittest.main()
