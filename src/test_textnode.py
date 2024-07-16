import unittest

from textnode import TextNode

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
        print(fuck_this)


if __name__ == "__main__":
    unittest.main()