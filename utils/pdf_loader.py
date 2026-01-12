"""
PDF document loader utility.
Uses PyPDF to extract text content from PDF files.
"""

from pypdf import PdfReader


def load_pdf(file_path: str) -> str:
    """
    Load a PDF file and extract all text content.

    Args:
        file_path: Path to the PDF file

    Returns:
        Extracted text content as a single string
    """
    try:
        reader = PdfReader(file_path)
        text_content = []

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text_content.append(page_text)

        return "\n".join(text_content)

    except FileNotFoundError:
        raise FileNotFoundError(f"PDF file not found: {file_path}")
    except Exception as e:
        raise Exception(f"Error reading PDF file: {e}")


def load_text_file(file_path: str) -> str:
    """
    Load a text file and return its content.

    Args:
        file_path: Path to the text file

    Returns:
        File content as string
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    except FileNotFoundError:
        raise FileNotFoundError(f"Text file not found: {file_path}")
    except Exception as e:
        raise Exception(f"Error reading text file: {e}")