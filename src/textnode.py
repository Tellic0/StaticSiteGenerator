class TextNode:
    def __init__(text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__ (TextNode1, TextNode2):
        if (
            TextNode1.text == TextNode2.text and
            TextNode1.text_type == TextNode2.text_type and
            TextNode1.url == TextNode2.url
        ):
            return True
        else:
            return False