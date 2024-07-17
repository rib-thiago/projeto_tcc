import os
import PyPDF2
from pdf2image import convert_from_path
from projeto.utils.exceptions import FileNotFoundError, IOError, PdfReadError, handle_exception

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError as e:
        handle_exception(FileNotFoundError(f"File not found: {file_path}"))
        return None
    except IOError as e:
        handle_exception(IOError(f"Error reading file: {file_path}"))
        return None

def write_file(file_path, content):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
    except IOError as e:
        handle_exception(IOError(f"Error writing to file: {file_path}"))

def verify_file_path(file_path):
    try:
        abs_path = os.path.abspath(file_path)
        if not os.path.isfile(abs_path):
            raise FileNotFoundError(f"File does not exist: {file_path}")
        if abs_path.endswith('.txt'):
            return 'txt'
        elif abs_path.endswith('.pdf'):
            return 'pdf'
        else:
            raise ValueError("Unsupported file type")
    except (FileNotFoundError, ValueError) as e:
        handle_exception(e)
        return None

def split_pdf(input_pdf_path, output_path_prefix):
    try:
        # Verifica se o arquivo PDF de entrada existe
        if not os.path.isfile(input_pdf_path):
            print(f"Arquivo '{input_pdf_path}' não encontrado.")
            return
        
        # Cria o diretório de saída, se ainda não existir
        os.makedirs(output_path_prefix, exist_ok=True)

        # Abre o arquivo PDF de entrada
        with open(input_pdf_path, 'rb') as input_file:
            # Cria um objeto PDFReader
            pdf_reader = PyPDF2.PdfReader(input_file)
            
            # Itera sobre cada página do PDF
            for page_number in range(len(pdf_reader.pages)):
                # Cria um novo PDFWriter para cada página
                pdf_writer = PyPDF2.PdfWriter()
                # Adiciona a página atual ao PDFWriter
                pdf_writer.add_page(pdf_reader.pages[page_number])

                # Escreve a página atual em um novo arquivo PDF
                output_pdf_path = os.path.join(output_path_prefix, f"page_{page_number + 1}.pdf")
                with open(output_pdf_path, 'wb') as output_file:
                    pdf_writer.write(output_file)
                    # print(f"Página {page_number + 1} extraída e salva em: {output_pdf_path}")

    except (FileNotFoundError, PdfReadError, IOError) as e:
        handle_exception(e)

def pdf_to_images(pdf_dir, output_folder):
    try:
        # Verificar se o diretório de saída existe, se não, criá-lo
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Lista para armazenar os caminhos das imagens PNG geradas
        image_paths = []

        # Iterar sobre todos os arquivos PDF no diretório fornecido
        for pdf_file in os.listdir(pdf_dir):
            pdf_path = os.path.join(pdf_dir, pdf_file)
            if pdf_path.endswith('.pdf'):
                # Converter cada página do PDF em imagens PNG
                images = convert_from_path(pdf_path)

                # Salvar as imagens no diretório de saída
                for i, image in enumerate(images):
                    image_path = os.path.join(output_folder, f"{os.path.splitext(pdf_file)[0]}_page_{i+1}.png")
                    image.save(image_path, "PNG")
                    image_paths.append(image_path)
                    # print(f"Imagem salva em: {image_path}")

        return image_paths

    except (IOError, PdfReadError) as e:
        handle_exception(e)
        return []
