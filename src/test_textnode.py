import unittest

from textnode import (
    TextNode, 
    text_node_to_html_node,
    text_type_text,
    text_type_bold,
    text_type_italic, 
    text_type_code, 
    text_type_link, 
    text_type_image
)

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_diff_types(self):
        node = TextNode("This is a text node", "italic")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)

    def test_diff_url(self):
        node = TextNode("This is a text node", "bold", "www.fuckthis.com")
        node2 = TextNode("This is a text node", "bold", "www.fuck_you.com")
        self.assertNotEqual(node, node2)

    def test_diff_url_None(self):
        node = TextNode("This is a text node", "italic", None)
        node2 = TextNode("This is a text node", "bold", None)
        self.assertNotEqual(node, node2)

    def test_diff_text(self):
        node = TextNode("I'm depressed", "italic")
        node2 = TextNode("Ready to go", "bold")
        self.assertNotEqual(node, node2)

    def test_rpr(self):
        node = TextNode("I'm depressed", "italic")
        node2 = TextNode("Ready to go", "bold")
        fuck_this = node.__repr__()
        # print(fuck_this)


    ############################
    # BOOT.DEV TESTS
    ############################

    def test_eq(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_text)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node2", text_type_text)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", text_type_italic, "https://www.boot.dev")
        node2 = TextNode(
            "This is a text node", text_type_italic, "https://www.boot.dev"
        )
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", text_type_text, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )

    ############################
    # MY TESTS
    ############################

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_to_html_function(self):
        node_italic = TextNode("I'm depressed", "italic")
        node2_bold = TextNode("Ready to go", "bold")
        node3_code = TextNode("def fuck()", "code")
        node4_link = TextNode("this is a link", "link", "www.getfucked.com")
        node5_img = TextNode("should be alt text", "image", "www.picture-link.com")

        # def __init__(self, text, text_type, url=None):
        #     self.text = text
        #     self.text_type = text_type
        #     self.url = url

        node1_italic = text_node_to_html_node(node_italic)
        node2 = text_node_to_html_node(node2_bold)
        node3 = text_node_to_html_node(node3_code)
        node4 = text_node_to_html_node(node4_link)
        node5 = text_node_to_html_node(node5_img)

        # print(f"Node 1: {node1_italic}")
        # print(f"Node 2: {node2}")
        # print(f"Node 3: {node3}")
        # print(f"Node 4: {node4}")
        # print(f"Node5: {node5}")

    def test_text_to_html_exception(self):
        node6_exception = TextNode("this should fuck up", "fart")

        with self.assertRaises(ValueError):
            text_node_to_html_node(node6_exception)


    ############################
    # BOOT.DEV TESTS
    ############################

    def test_text(self):
        node = TextNode("This is a text node", text_type_text)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", text_type_image, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", text_type_bold)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")


if __name__ == "__main__":
    unittest.main()