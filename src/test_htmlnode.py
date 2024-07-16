import unittest

from htmlnode import HTMLNode

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
        print(f"I FUCKING HATE THIS: {fuck_this}")

    def test_print(self):
        node2 = HTMLNode()
        node3 = HTMLNode()
        node = HTMLNode("p", "i hate this", [node2, node3], {"href": "https://www.fuckthis.com", 
    "target": "_blank",
})
        fuck_this = node.__repr__()
        print(fuck_this)



if __name__ == "__main__":
    unittest.main()