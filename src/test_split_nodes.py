import unittest

from textnode import TextNode
import re
from split_nodes import split_nodes_delimiter

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


class TestSplitNode(unittest.TestCase):
    node = TextNode("This is text with a `code block` word", text_type_text)
    node2 = TextNode("This is text with a **bold** word", text_type_text)
    node3 = TextNode("This is text with an *italic* word", text_type_text)
    node4 = TextNode("This is text with a `code block` word", text_type_text)
    # code_nodes = split_nodes_delimiter([node], "`", text_type_code)
    # bold_nodes = split_nodes_delimiter([node2], "**", text_type_bold)

    # print(f"Code Nodes: {code_nodes}")
    # print(f"Bold node: {bold_nodes}")

    def test_delimiter_error_open(self):
        node_error = TextNode("This is text with a **bold error", text_type_text)
        with self.assertRaises(Exception):
            print(split_nodes_delimiter([node_error], "**", text_type_bold))
            split_nodes_delimiter([node_error], "**", text_type_bold)

    def test_delimiter_error_close(self):
        node_error = TextNode("This is text with a bold** error", text_type_text)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node_error], "**", text_type_bold)

    def test_delimiter_error_mismatch(self):
        node_error = TextNode("This is text with a *bold** error", text_type_text)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node_error], "**", text_type_bold)

    # def test_link(self):
    #     node2 = TextNode("This is text with a [link](https://www.deeznuts.com)", text_type_link)

    #     fart = split_nodes_delimiter([node2], "", text_type_link)

    #     test = [TextNode("This is text with a ", text_type_text, None), TextNode('**bold**', text_type_bold, None), TextNode(' word', text_type_text, None)]

    #     self.assertEqual(fart, test)


#########################
# BOOT.DEV TESTS
########################


    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded word", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        # print(f"New Nodes1: {new_nodes}")
        new_nodes = split_nodes_delimiter(new_nodes, "*", text_type_italic)
        # print(f"New Nodes2: {new_nodes}")
        self.assertListEqual(
            [
                TextNode("bold", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("italic", text_type_italic),
            ],
            new_nodes,
        )



if __name__ == "__main__":
    unittest.main()
