import cv2
import pytesseract


def ocr_extract_text(image_path, language='eng'):
    try:
        # Carregar a imagem usando OpenCV
        img = cv2.imread(image_path)

        # Converter a imagem para escala de cinza (opcional, dependendo da qualidade da imagem)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Aplicar thresholding para melhorar o contraste (opcional)
        _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # Aplicar OCR usando Tesseract
        resultado = pytesseract.image_to_string(thresh, lang=language)

        return resultado.strip()  # Retorna o texto extraído, removendo espaços em branco desnecessários

    except Exception as e:
        print(f"Erro ao extrair texto usando OCR: {e}")
        return ""
