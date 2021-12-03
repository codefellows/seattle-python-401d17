from linked_list.linked_list import Node, LinkedList


def test_create_node():
    node = Node("apple")
    actual = node.value
    expected = "apple"
    assert actual == expected


def test_node_next_default():
    node = Node("apple")
    actual = None
    expected = node.next
    assert actual == expected


def test_node_next_something():
    apple = Node("apple")
    banana = Node("banana", apple)
    actual = banana.next
    expected = apple
    assert actual == expected


def test_create_linked_list():
    lst = LinkedList()
    assert lst.head is None


def test_insert_when_empty():
    lst = LinkedList()
    lst.insert("apple")
    assert lst.head.value == "apple"


def test_insert_when_not_empty():
    lst = LinkedList()
    lst.insert("apple")
    lst.insert("banana")
    assert lst.head.value == "banana"
    assert lst.head.next.value == "apple"


def test_includes_true():
    lst = LinkedList()
    lst.insert("apple")
    lst.insert("banana")
    actual = lst.includes("apple")
    expected = True
    assert actual == expected


def test_includes_false():
    lst = LinkedList()
    lst.insert("apple")
    lst.insert("banana")
    actual = lst.includes("cucumber")
    expected = False
    assert actual == expected


def test_to_string():
    lst = LinkedList()
    lst.insert("apple")
    lst.insert("banana")
    assert str(lst) == "{ banana } -> { apple } -> NULL"
