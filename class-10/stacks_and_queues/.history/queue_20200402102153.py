from invalid_operation_error import InvalidOperationError
from node import Node


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
            raise InvalidOperationError("Method not allowed on empty collection")

        temp = self.front

        self.front = self.front.next

        temp.next = None

        return temp.value

    def peek(self):

        if not self.front:
            raise InvalidOperationError("Method not allowed on empty collection")

        return self.front.value

    def is_empty(self):
        return self.front == None
