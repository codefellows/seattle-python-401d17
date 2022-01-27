class FancyLinkedList:
    def __init__(self, collection=None):
        self.head = None
        if collection:

            # Converts
            # [a,b,c] into
            # [a] -> [b] -> [c] -> None

            for item in reversed(collection):
                self.insert(item)

    def __str__(self):

        out = ""

        for value in self:
            out += f"[ {value} ] -> "

        return out + "None"

    def insert(self, value):
        self.head = Node(value, self.head)

    def __iter__(self):
        def value_generator():
            current = self.head
            while current:
                yield current.value
                current = current.next

        return value_generator()

    def __len__(self):
        # return len(list(iter(self)))
        count = 0
        for item in self:
            count += 1

        return count

    def __eq__(self, other):
        return list(self) == list(other)

    def __getitem__(self, index):
        if index < 0:
            raise IndexError

        for i, item in enumerate(self):
            if i == index:
                return item

        raise IndexError

    def __setitem__(self, index, value):
        current = self.head

        while current:
            pass


class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


if __name__ == "__main__":
    linked_nums = FancyLinkedList(collection=[1, 2, 3, 4, 5])

    print(linked_nums)

    for num in linked_nums:
        print(num)
