import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


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

    def test_to_html_several_children(self):
        child_node = LeafNode("span", "child")
        child_node1 = LeafNode("b", "child1")
        parent_node = ParentNode("div", [child_node, child_node1])
        self.assertEqual(
            parent_node.to_html(), "<div><span>child</span><b>child1</b></div>"
        )

    def test_to_html_nested_parent_inside_parent(self):
        child_node = LeafNode("b", "child")
        inner_parent_node = ParentNode("p", [child_node])
        outer_parent_node = ParentNode("div", [inner_parent_node])
        self.assertEqual(outer_parent_node.to_html(), "<div><p><b>child</b></p></div>")

    def test_to_html_missing_children(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError) as error:
            parent_node.to_html()

        self.assertEqual(str(error.exception), "Parent Node without children")


if __name__ == "__main__":
    unittest.main()
