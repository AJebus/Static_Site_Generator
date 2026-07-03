import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_different_types(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_one_has_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode(
            "This is a text node",
            TextType.BOLD,
            "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/EDMggme-800x370.png",
        )
        self.assertNotEqual(node, node2)

    def test_different_texts(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
