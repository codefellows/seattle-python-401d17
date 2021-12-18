from tree.binary_search_tree import BinarySearchTree
from tree.binary_tree import BinaryTree
from tree.node import Node


def test_binary_search_tree():
    bst = BinarySearchTree()
    assert isinstance(bst, BinaryTree)


def test_add_child():
    # Can successfully add a left child and right child to a single root node
    ten = Node(10)
    bst = BinarySearchTree(ten)
    bst.add(5)
    bst.add(15)

    assert bst.root.value == 10
    assert bst.root.left.value == 5
    assert bst.root.right.value == 15


def test_add_child_more():
    # Can successfully add a left child and right child to a single root node
    ten = Node(10)
    bst = BinarySearchTree(ten)
    bst.add(5)
    bst.add(15)
    bst.add(7)
    bst.add(25)

    assert bst.root.value == 10
    assert bst.root.left.value == 5
    assert bst.root.right.value == 15
    assert bst.root.left.right.value == 7
    assert bst.root.right.right.value == 25
