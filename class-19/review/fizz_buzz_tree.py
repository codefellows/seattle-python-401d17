from collections import deque


def fizz_buzz_tree(tree):
    """
    most flexible way is to clone tree and convert each
    value via the given fizzify converter function
    """
    return tree.clone(fizzify)


def fizz_buzz_tree_longer(tree):
    """
    Less flexible fizz buzz but perhaps easier
    to comprehend
    """
    fizzy_root = fizzy_copy(tree.root)

    pairs = Queue()
    pairs.enqueue((tree.root, fizzy_root))

    while not pairs.is_empty():
        source_front, fizzy_front = pairs.dequeue()

        for source_child in source_front.children:
            fizzy_child = fizzy_copy(source_child)
            fizzy_front.children.append(fizzy_child)
            pair = (source_child, fizzy_child)
            pairs.enqueue(pair)

    return KaryTree(fizzy_root)


def fizzy_copy(node):
    fizzy_value = fizzify(node.value)
    return Node(fizzy_value)


def fizzify(value):
    """
    Converts given value in the fizz buzz way
    """
    fizzy_value = ""
    if value % 3 == 0:
        fizzy_value += "Fizz"

    if value % 5 == 0:
        fizzy_value += "Buzz"

    return fizzy_value or str(value)


def fizzify_seven(value):
    """
    Like fizz buzz but handles multiples of seven too
    """
    fizzy_value = ""
    if value % 3 == 0:
        fizzy_value += "Fizz"

    if value % 5 == 0:
        fizzy_value += "Buzz"

    if value % 7 == 0:
        fizzy_value += "hip hop hippity...."

    return fizzy_value or str(value)


class Queue:
    """Queue implementation using deque under the hood"""

    def __init__(self):
        self.storage = deque()

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        if self.is_empty():
            raise EmptyError(self.dequeue)

        return self.storage.popleft()

    def peek(self):
        if self.is_empty():
            raise EmptyError(self.peek)

        return self.storage[0]

    def is_empty(self):
        return len(self.storage) == 0


class EmptyError(Exception):
    def __init__(self, method):
        super().__init__(
            f"Cannot call {method.__name__} method on empty Queue"
        )


class KaryTree:
    def __init__(self, root=None):
        self.root = root

    def to_list(self):
        queue = Queue()

        collection = []

        queue.enqueue(self.root)

        while not queue.is_empty():
            node = queue.dequeue()
            collection.append(node.value)  # do something
            for child in node.children:
                queue.enqueue(child)

        return collection

    def clone(self, converter=None):
        """
        return clone of self
        applies optional converter function to value of each node
        which is handy for things like fizz_buzz ;)
        """

        clone_root = self.root.clone(converter)
        clone_tree = KaryTree(clone_root)

        pairs = Queue()

        pairs.enqueue((self.root, clone_root))

        while not pairs.is_empty():
            source_node, clone_node = pairs.dequeue()
            for source_child_node in source_node.children:
                clone_child_node = source_child_node.clone(converter)
                pair = (source_child_node, clone_child_node)
                pairs.enqueue(pair)
                clone_node.children.append(clone_child_node)

        return clone_tree


class Node:
    """K-Ary Tree Node"""

    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []

    def clone(self, converter=None):
        value = self.value

        if converter:
            value = converter(value)

        return Node(value)
