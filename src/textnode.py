text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eg__(self, TextNode2):
            return (self.text == TextNode2.text 
                    and self.text_type == TextNode2.text_type 
                    and self.url == TextNode2.url)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"