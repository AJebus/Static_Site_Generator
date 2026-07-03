import unittest
from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        htmlprops = ' href="https://www.google.com" target="_blank"'
        node = HTMLNode("<h1>", "This is a HTML node", [], props)
        self.assertEqual(node.props_to_html(), htmlprops)

    def test_props_to_html_blank(self):
        props = {}
        htmlprops = ""
        node = HTMLNode("<h1>", "This is a HTML node", [], props)
        self.assertEqual(node.props_to_html(), htmlprops)

    def test_props_to_html_None(self):
        props = None
        htmlprops = ""
        node = HTMLNode("<h1>", "This is a HTML node", [], props)
        self.assertEqual(node.props_to_html(), htmlprops)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_to_html_props(self):
        node = LeafNode("a", "Hello, world!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(), '<a href="https://www.google.com">Hello, world!</a>'
        )


if __name__ == "__main__":
    unittest.main()
