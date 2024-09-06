from writers import writer
from io import BytesIO
from fpdf import FPDF


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
            # pdf.cell()

            pdf_bytes = pdf.output(dest="S").encode("latin1")
            pdf_buffer = BytesIO(pdf_bytes)

            return pdf_buffer, filename

        except Exception as e:
            print(f"error -> {str(e)}")
            return ""
