from textnode import TextType, TextNode
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            if node.text.count(delimiter) % 2 == 0:
                if node.text.count(delimiter) == 0:
                    new_nodes.append(node)
                else:
                    parts = node.text.split(delimiter)
                    for i in range(len(parts)):
                        if i % 2 == 1:
                            if parts[i] == "":
                                continue
                            new_nodes.append(TextNode(parts[i], text_type))
                        else:
                            if parts[i] == "":
                                continue
                            new_nodes.append(TextNode(parts[i], TextType.TEXT))
            else:
                raise Exception("Invalid Markdown, unmatched delimiter found")
        else:
            new_nodes.append(node)
    print(new_nodes)
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)    

