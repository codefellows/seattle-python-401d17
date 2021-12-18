from tree.binary_tree import BinaryTree
from tree.node import Node

# DONE: Can successfully instantiate an empty tree
# DONE: Can successfully instantiate a tree with a single root node

# DONE: Can successfully return a collection from a preorder traversal
# DONE: Can successfully return a collection from an inorder traversal
# DONE: Can successfully return a collection from a postorder traversal

# Can successfully add a left child and right child to a single root node


def test_binary_tree_empty():
    tree = BinaryTree()
    assert tree


def test_binary_tree_with_root():
    apple = Node("apple")
    tree = BinaryTree(apple)
    actual = tree.root.value
    expected = "apple"
    assert actual == expected


def test_pre_order():
    apple = Node("apple")
    apple.left = Node("banana")
    apple.right = Node("cucumber")

    #          apple
    #   banana       cucumber

    tree = BinaryTree(apple)
    expected = ["apple", "banana", "cucumber"]
    actual = tree.pre_order()

    assert actual == expected


def test_in_order():
    apple = Node("apple")
    apple.left = Node("banana")
    apple.right = Node("cucumber")

    #          apple
    #   banana       cucumber

    tree = BinaryTree(apple)
    expected = ["banana", "apple", "cucumber"]
    actual = tree.in_order()

    assert actual == expected


def test_post_order():
    apple = Node("apple")
    apple.left = Node("banana")
    apple.right = Node("cucumber")

    #          apple
    #   banana       cucumber

    tree = BinaryTree(apple)
    expected = ["banana", "cucumber", "apple"]
    actual = tree.post_order()

    assert actual == expected
