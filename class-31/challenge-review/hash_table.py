from codefellows.dsa.linked_list import LinkedList


class HashTable:
    def __init__(self):
        self.buckets = [None] * 1024

    def get(self, key):
        pass

    def add(self, key, value):
        hash = self.hash(key)
        bucket = self.buckets[hash]
        if bucket is None:
            bucket = LinkedList()
            self.buckets[hash] = bucket
        bucket.append((key, value))
        # TODO handle RE add (aka update)

    def contains(self, key):
        pass

    def hash(self, key):
        return sum([ord(char) for char in key]) * 599 % len(self.buckets)
