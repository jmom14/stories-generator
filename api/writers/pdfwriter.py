from writers import writer
from io import BytesIO
from fpdf import FPDF
import logging


class PDFWriter(writer.Writer):

    def __init__(self, title: str, author: str, content: str):
        self.title = title
        self.author = author
        self.content = content

    def write(self):
        try:
            filename = "_".join(self.title.split(" ")) + ".pdf"
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=18)
            pdf.cell(200, 10, txt=self.title, ln=True, align="C")

            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, txt=self.content)

            pdf_bytes = pdf.output(dest="S").encode("latin1")
            pdf_buffer = BytesIO(pdf_bytes)

            return pdf_buffer, filename

        except Exception as e:
            logging.error(str(e))
            return ""
