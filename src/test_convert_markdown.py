import unittest

from textnode import TextNode, TextType
from convert_markdown import split_nodes_delimiter


class TestconvertMarkdown(unittest.TestCase):
    def test_split_nodes_delimiter_code_simple(self):
        node = TextNode("This is `code` here", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)

        assert len(result) == 3
        assert result[0].text == "This is "
        assert result[0].text_type == TextType.TEXT

        assert result[1].text == "code"
        assert result[1].text_type == TextType.CODE

        assert result[2].text == " here"
        assert result[2].text_type == TextType.TEXT

    def test_split_nodes_delimiter_bold_simple(self):
        node = TextNode("This is **bold** here", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)

        assert len(result) == 3
        assert result[0].text == "This is "
        assert result[0].text_type == TextType.TEXT

        assert result[1].text == "bold"
        assert result[1].text_type == TextType.BOLD

        assert result[2].text == " here"
        assert result[2].text_type == TextType.TEXT    


    def test_split_nodes_delimiter_bold_double(self):
        node = TextNode("This is **bold** here and **bold2**", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)

        assert len(result) == 4
        assert result[0].text == "This is "
        assert result[0].text_type == TextType.TEXT

        assert result[1].text == "bold"
        assert result[1].text_type == TextType.BOLD

        assert result[2].text == " here and "
        assert result[2].text_type == TextType.TEXT   

        assert result[3].text == "bold2"
        assert result[3].text_type == TextType.BOLD        

   

if __name__ == "__main__":
    unittest.main()








