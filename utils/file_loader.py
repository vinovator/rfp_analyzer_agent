import fitz #PyMuPDF
import docx2txt
import os


def load_pdf(file_path):
    """
    Load text from a PDF file.
    
    :param file_path: Path to the PDF file.
    :return: Extracted text from the PDF.
    """
    text = ""
    try:
        with fitz.open(file_path) as pdf_document:
            for page in pdf_document:
                text += page.get_text()
    except Exception as e:
        print(f"Error reading PDF file {file_path}: {e}")
    return text


def load_docx(file_path):
    """
    Load text from a DOCX file.
    
    :param file_path: Path to the DOCX file.
    :return: Extracted text from the DOCX.
    """
    try:
        text = docx2txt.process(file_path)
        return text
    except Exception as e:
        print(f"Error reading DOCX file {file_path}: {e}")
        return ""