text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

from htmlnode import LeafNode

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other_node):
        return (
            self.text == other_node.text
            and self.text_type == other_node.text_type
            and self.url == other_node.url
        )
    
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


# super().__init__(tag, value, children=None, props=props)
def text_node_to_html_node(text_node):
    match(text_node.text_type):
        case "text":
            return LeafNode(None, text_node.text)
        case "bold":
            return LeafNode("b", text_node.text)
        case "italic":
            return LeafNode("i", text_node.text)
        case "code":
            return LeafNode("code", text_node.text)
        case "link":
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case "image":
            return LeafNode("img", '', {"src": text_node.url, "alt": text_node.text})
        case __:
            raise ValueError(f"Invalid text type: {text_node.text_type}")


def main():
    text_test = TextNode("fuck this", "bold", "www.fuckoff.com")
    text_test.__repr__()


main()