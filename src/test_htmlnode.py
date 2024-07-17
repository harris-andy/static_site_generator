import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

# def __init__(self, tag=None, value=None, children=None, props=None)
    
class Test_HTML_Node(unittest.TestCase):
    def test_eq(self):
        node3 = HTMLNode()
        node2 = node = HTMLNode("p", "i hate this", [node3], {"href": "https://www.fuckthis.com", 
    "target": "_blank",
})
        node = HTMLNode("p", "i hate this", [node2, node3], {"href": "https://www.fuckthis.com", 
    "target": "_blank",
})
        
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        node2 = HTMLNode()
        node3 = HTMLNode()
        node = HTMLNode("p", "i hate this", [node2, node3], {
    "href": "https://www.fuckthis.com", 
    "target": "_blank",
})
        fuck_this = node.props_to_html()
        expected_html = ' href="https://www.fuckthis.com" target="_blank"'
        self.assertEqual(fuck_this, expected_html)


    def test_print(self):
        node2 = HTMLNode()
        node3 = HTMLNode()
        node = HTMLNode("p", "i hate this", [node2, node3], {"href": "https://www.fuckthis.com", 
    "target": "_blank",
})
        fuck_this = node.__repr__()
        # print(f"FUCK THIS: {fuck_this}")
        expected_html = "HTML Node Object: tag: p, value: i hate this, children: [HTML Node Object: tag: None, value: None, children: None, props: {}, HTML Node Object: tag: None, value: None, children: None, props: {}], props: {'href': 'https://www.fuckthis.com', 'target': '_blank'}"
        self.assertEqual(fuck_this, expected_html)


    # TEST LEAF NODES

    def test_leafnode_creation(self):
        # Test creation of LeafNode
        leaf_node = LeafNode(tag="div", value="Content", props={"class": "container"})
        self.assertEqual(leaf_node.tag, "div")
        self.assertEqual(leaf_node.value, "Content")
        self.assertEqual(leaf_node.props, {"class": "container"})
        self.assertIsNone(leaf_node.children)  # Ensure children is None for LeafNode

    def test_to_html(self):
        leaf_node = LeafNode(tag="div", value="Content", props={"class": "container"})
        result = leaf_node.to_html()
        expected = '<div class="container">Content</div>'
        self.assertEqual(result, expected)
        
    def test_to_html_no_value(self):
        leaf_node = LeafNode(tag="div", props={"class": "container"})
        leaf_node.to_html()

    def test_to_html_no_value(self):
        with self.assertRaises(ValueError):
            LeafNode(tag="div", props={"class": "container"}).to_html()


    # TEST PARENT NODES
    # class ParentNode(HTMLNode):
    # def __init__(self, tag=None, children=None, props=None) -> None:
    #     super().__init__(tag, value=None, children=children, props=props)
    
    def test_parent_node_to_html(self):
        node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)
        children_text = node.to_html()
        # print(f"CHILDREN TEXT: {children_text}")
        self.assertEqual(children_text, "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")


    def test_parent_node_nested_parent_nodes(self):
        child_node1 = LeafNode("i", "bullshit")
        child_node2 = LeafNode("b", "stupid")
        node = ParentNode(
    "p",
    [
        ParentNode("b", [child_node1, child_node2]),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)
        actual_html = node.to_html()
        expected_html = (
            '<p><b><i>bullshit</i><b>stupid</b></b>'
            'Normal text<i>italic text</i>Normal text</p>'
        )
        self.assertEqual(actual_html, expected_html)
        print(f"Generated HTML: {actual_html}")

    
    def test_parent_node_no_children(self):
        child_node1 = LeafNode("i", "bullshit")
        child_node2 = LeafNode("b", "stupid")
        node = ParentNode(
    "p"
)
        self.assertRaises(ValueError)

    
    def test_parentNode_with_props(self):
        child_node1 = LeafNode("i", "bullshit")
        child_node2 = LeafNode("b", "stupid")
        child_node3 = LeafNode("h1", "fuck")
        child_node4 = LeafNode("h2", "this")
        node = ParentNode(
    "p",
    [
        ParentNode("b", [child_node1, child_node2]),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        ParentNode("h4", [child_node3, child_node4]),
    ],
    {
    "href": "https://www.google.com", 
    "target": "_blank",
    }
    )
        actual_html = node.to_html()
        expected_html = expected_html = (
    '<p href="https://www.google.com" target="_blank">'
    '<b><i>bullshit</i><b>stupid</b></b>'
    'Normal text'
    '<i>italic text</i>'
    '<h4><h1>fuck</h1><h2>this</h2></h4>'
    '</p>'
)

        self.assertEqual(actual_html, expected_html)
    


if __name__ == "__main__":
    unittest.main()