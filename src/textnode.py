from enum import Enum

class TextType(Enum):
    text = "plain"
    bold_text = "bold"
    italic_text = "italic"
    code_text = "code"
    link = "link"
    image = "image"

class TextNode:
    def __init__(self, content: str, text_type: str, url: str | None):
        self.text = content
        self.text_type = TextType(text_type)
        self.url = url

    def __eq__(self, other: TextNode):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
