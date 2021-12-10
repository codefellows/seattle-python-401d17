from codefellows.dsa.linked_list import LinkedList


class MyLinkedList(LinkedList):
    def kth_from_end(self, k):
        leader = self.head
        follower = None

        steps_ahead = 0

        while leader:
            leader = leader.next

            if follower:
                follower = follower.next
            elif steps_ahead == k:
                follower = self.head
            else:
                steps_ahead += 1

        if not follower:
            raise IndexError(f"k is out of range: {k}")

        return follower.value


linked = MyLinkedList(values=[1, 2, 3])

result = linked.kth_from_end(0)

assert result == 3


result = linked.kth_from_end(1)

assert result == 2

result = linked.kth_from_end(2)

assert result == 1

try:
    result = linked.kth_from_end(3)
except IndexError:
    print("good, 3 was caught")

try:
    result = linked.kth_from_end(-1)
except IndexError:
    print("good, -1 was caught")

print("TESTS PASSED")
