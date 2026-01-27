import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_basic(self):
        node = HTMLNode("a", "link", None, {"href": "https://example.com"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com"')
        node = HTMLNode("h1", "link", "stuff", {"href": "https://example.com", "tag": "important"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com" tag="important"')

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        node2 = LeafNode("a", "This is a Link!", {"href": "https://google.com"})
        self.assertEqual(node2.to_html(), '<a href="https://google.com">This is a Link!</a>')


if __name__ == "__main__":
    unittest.main()
