class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        """
        Arguments: value
        Returns: nothing
        Adds a new node with that value to the head of the list
        with an O(1) Time performance.
        """

        self.head = Node(value, self.head)

        # Or...
        # node = Node(value)
        # node.next = self.head

        # self.head = node

    def includes(self, value):
        """See if value is contained in LinkedList

        Args:
            value (any): the value being searched for

        Returns:
            Boolean: True if found, else False
        """

        current = self.head

        while current:
            if current.value == value:
                return True
            current = current.next

        return False

    def __str__(self):

        current = self.head

        output = ""

        while current:

            output += "{ " + current.value + " } -> "

            current = current.next

        output += "NULL"

        return output
