from tree.binary_tree import BinaryTree
from tree.node import Node


class BinarySearchTree(BinaryTree):
    def add(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node

        def walk(root, node_to_add):
            if root is None:
                return

            if node_to_add.value < root.value:
                if root.left:
                    walk(root.left, node_to_add)
                else:
                    root.left = node_to_add

            else:
                if root.right:
                    walk(root.right, node_to_add)
                else:
                    root.right = node_to_add

        walk(self.root, node)

    def contains(self, value):
        pass
