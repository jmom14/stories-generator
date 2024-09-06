from writers import writer
from ebooklib import epub


class EPUBWriter(writer.Writer):

    def __init__(self, title: str, author: str, content: str):
        self.title = title
        self.author = author
        self.content = content

    def write(self):
        filename = "_".join(self.title.split(" ")) + ".epub"
        book = epub.EpubBook()
        book.set_identifier("id123456")
        book.set_title(self.title)
        book.set_language("en")
        book.add_author(self.author)

        c1 = epub.EpubHtml(title="Intro", file_name="chap_01.xhtml", lang="hr")
        content = f"<h1>{self.title}</h1>" f"<p>{self.content}</p>"
        c1.content = content
        book.add_item(c1)
        book.toc = (
            epub.Link("chap_01.xhtml", "Introduction", "intro"),
            (epub.Section("Simple book"), (c1,)),
        )
        book.add_item(epub.EpubNcx())
        book.add_item(epub.EpubNav())
        style = "BODY {color: white;}"

        nav_css = epub.EpubItem(
            uid="style_nav",
            file_name="style/nav.css",
            media_type="text/css",
            content=style,
        )

        book.add_item(nav_css)
        book.spine = ["nav", c1]

        try:
            print("filename epub -> ", filename)
            epub.write_epub(filename, book, {})
            return "", filename
        except Exception as e:
            print(str(e))
            print("error epub")
            return ""
