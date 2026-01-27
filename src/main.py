from textnode import TextNode, TextType

def main():
    node = TextNode("Test", TextType.LINK, "https://boot.dev")
    print(node)

if __name__ == "__main__":
    main()
