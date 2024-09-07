from writers.epubwriter import EPUBWriter
from writers.pdfwriter import PDFWriter
from enum import Enum


class Format(Enum):
    EPUB = "epub"
    PDF = "pdf"


media_type_options = {
    "epub": "application/epub+zip",
    "pdf": "application/pdf",
}


def get_media_type(file_format: str):
    return media_type_options.get(file_format, "application/octet-stream")


class WriterFactory:

    def __init__(self, file_format):
        self.format = file_format

    def create_writer(self, title, author, content):
        if self.format == Format.EPUB.value:
            return EPUBWriter(title, author, content)
        elif self.format == Format.PDF.value:
            return PDFWriter(title, author, content)
        else:
            raise ValueError("Unsupported format, choose either EPUB or PDF.")
