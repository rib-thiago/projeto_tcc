class CustomException(Exception):
    """Base class for custom exceptions"""
    pass

class FileNotFoundError(CustomException):
    """Raised when the file is not found"""
    pass

class IOError(CustomException):
    """Raised when an I/O operation fails"""
    pass

class PdfReadError(CustomException):
    """Raised when there is an error reading a PDF file"""
    pass

def handle_file_not_found_error(file_path):
    """Handles the FileNotFoundError exception"""
    print(f"File not found error occurred: File does not exist: {file_path}")
    input("Pressione Enter para continuar...")

def handle_io_error(file_path):
    """Handles the IOError exception"""
    print(f"I/O error occurred: Error reading or writing file: {file_path}")
    input("Pressione Enter para continuar...")

def handle_pdf_read_error(file_path):
    """Handles the PdfReadError exception"""
    print(f"PDF read error occurred: Error reading PDF file: {file_path}")
    input("Pressione Enter para continuar...")

def handle_exception(exception):
    """Centralized exception handling function"""
    if isinstance(exception, FileNotFoundError):
        handle_file_not_found_error(exception.args[0])
    elif isinstance(exception, IOError):
        handle_io_error(exception.args[0])
    elif isinstance(exception, PdfReadError):
        handle_pdf_read_error(exception.args[0])
    else:
        print("An unexpected error occurred:", exception)
        input("Pressione Enter para continuar...")
