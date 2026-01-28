import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
        "<div><span><b>grandchild</b></span></div>",
    )



if __name__ == "__main__":
    unittest.main()
