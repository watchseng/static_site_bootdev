import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_basic(self):
        node = HTMLNode("a", "link", None, {"href": "https://example.com"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com"')
        
        node = HTMLNode("h1", "link", "stuff", {"href": "https://example.com", "tag": "important"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com" tag="important"')



if __name__ == "__main__":
    unittest.main()
