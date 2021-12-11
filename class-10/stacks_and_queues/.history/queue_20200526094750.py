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
        self._storage = LinkedList()
        self._front = None
        self._rear = None


    def enqueue(self, value):
        
        node = Node(value)

        if self._rear:
            pass
        else:
            self._rear = self._front = node

    def dequeue(self):
        pass

    def peek(self):

        if not self._front:
            raise InvalidOperationError("Cannot peek an empty stack")

        return self._front.value

    def is_empty(self):

        return not self._front



if __name__ == "__main__":
    colors = Queue()
    assert colors.is_empty()

    colors.enqueue("green")
    assert colors.is_empty() == False
    assert colors.peek() == "green"
    assert colors._front.value == "green"
    assert colors._rear.value == "green"

    # colors.enqueue("pink")
    # assert colors._front.value == "green"
    # assert colors._rear.value == "pink"





    print("******* All good!!! ************")