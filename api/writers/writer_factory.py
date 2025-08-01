from api.writers.epubwriter import EPUBWriter
from api.writers.pdfwriter import PDFWriter
from enum import Enum


class Format(Enum):
    EPUB = "epub"
    PDF = "pdf"


media_type_options = {
    "epub": "application/epub+zip",
    "pdf": "application/pdf",
    "generic": "application/octet-stream",  # Default for unknown formats
}


def get_media_type(file_format: str) -> str:
    defult_format = media_type_options["generic"]
    return media_type_options.get(file_format, defult_format)


class WriterFactory:

    @staticmethod
    def get_writer(file_format: str, title: str, author: str, content: str):
        if file_format == Format.EPUB.value:
            return EPUBWriter(title, author, content)
        elif file_format == Format.PDF.value:
            return PDFWriter(title, author, content)
        else:
            raise ValueError("Unsupported format, choose either EPUB or PDF.")
