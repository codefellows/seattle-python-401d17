class LinkedList:
    pass

class InvalidOperationError(Exception):
    pass

class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_

class Queue:
    def __init__(self):
        self.storage = LinkedList()
        self.front = None


    def enqueue(self, value):
        pass

    def dequeue(self):
        pass

    def peek(self):

        if not self.front:
            raise InvalidOperationError("Cannot peek an empty stack")

        return self.front.value

    def is_empty(self):

        return not self.front



if __name__ == "__main__":
    colors = Queue()
    assert not colors.is_empty()
    print("******* All good!!! ************")