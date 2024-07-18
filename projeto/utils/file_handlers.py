import os
import PyPDF2
from pdf2image import convert_from_path


def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

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

    except FileNotFoundError:
        print(f"Arquivo '{input_pdf_path}' não encontrado.")
    except Exception as e:
        print(f"Erro ao processar o PDF: {e}")

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

    except FileNotFoundError:
        print(f"Arquivo '{pdf_dir}' não encontrado.")
        return []
    except Exception as e:
        print(f"Erro ao processar o PDF: {e}")
        return []
