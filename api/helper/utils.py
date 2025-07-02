import re


def extract_markdown_content(markdown_text: str) -> str:
    return markdown_text.strip("`json\n").strip("`")


def sanitize_filename(name: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_\-]", "_", name)
