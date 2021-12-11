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
        self.rear = None


    def enqueue(self, value):
        
        node = Node(value)

        if self.rear:
            pass
        else:
            self.rear = self.front = node

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
    assert colors.is_empty()

    colors.enqueue("green")
    assert colors.is_empty() == False
    assert colors.peek() == "green"

    print("******* All good!!! ************")