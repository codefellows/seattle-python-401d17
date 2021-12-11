"""Stack, Queue, and the other classes to support them"""


class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


class InvalidOperationError(Exception):
    pass


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        self.top = Node(value, self.top)

    def pop(self):

        if not self.top:
            raise InvalidOperationError(
                "Method not allowed on empty collection"
            )

        popped = self.top

        self.top = self.top.next

        return popped.value

    def is_empty(self):
        return self.top is None

    def peek(self):

        if not self.top:
            raise InvalidOperationError(
                "Method not allowed on empty collection"
            )

        return self.top.value


class Queue:
    """
    Queue data structure implementation
    Note: helps to remember that the "rear" is like the "head" of a LinkedList
    and the "front" node will always have a next of None
    """

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)

        if self.rear:
            self.rear.next = node

        self.rear = node

        self.front = self.front or self.rear

    def dequeue(self):

        if not self.front:
            raise InvalidOperationError(
                "Method not allowed on empty collection"
            )

        temp = self.front

        self.front = self.front.next

        temp.next = None

        return temp.value

    def peek(self):

        if not self.front:
            raise InvalidOperationError(
                "Method not allowed on empty collection"
            )

        return self.front.value

    def is_empty(self):
        return self.front is None
