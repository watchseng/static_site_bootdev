import unittest

from textnode import TextNode, TextType
from textnode_to_htmlnode import text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")

        node = TextNode("This is a italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a italic node")

    def test_image_node_to_html(self):
        node = TextNode("A bear", TextType.IMAGE, "https://example.com/bear.png")
        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://example.com/bear.png", "alt": "A bear"},
            )


    def test_link_node_to_html(self):
        node = TextNode("Click me", TextType.LINK, "https://boot.dev")
        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click me")
        self.assertEqual(html_node.props, {"href": "https://boot.dev"})


if __name__ == "__main__":
    unittest.main()