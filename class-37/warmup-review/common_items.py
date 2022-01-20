from codefellows.dsa.linked_list import LinkedList
# BIG NOTE: This LinkedList supports iteration, which allows for certain cool things

def get_common_items(linked_a, linked_b):
    common = [] # O(1), O(1)
    # biggest could get is size of smaller min(a,b)
    # your code
    values_a = set() # O(1) Time and Space
    values_b = set() # O(1) Time and Space

    current = linked_a.head # O(1) Time and Space

    # linked a iteration O(a)
    while current: # O(a) Time and Space
        values_a.add(current.value) # O(1)
        current = current.next # O(1)
        # values_a is getting as big as linked_a

    # O(a) = size of linked_a
    # O(b) = size of linked_b

    # linked b iteration O(b)
    current = linked_b.head
    while current:
        values_b.add(current.value)
        current = current.next

    # loop through values_a
    for value in values_a: #Time O(a)
        if value in values_b: # Time O(1)
            common.append(value) # Time O(1)


    # values_a space O(a)
    # values_b space O(b)
    # common space smaller of O(a) or O(b)

    return common

def common_fancy(linked_a, linked_b):
    for value in linked_a: # a
        if value in linked_b: # b





















def get_common_items_before_class(linked_a, linked_b):
    common = []
    values_a = set()

    current = linked_a.head
    while current:
        values_a.add(current.value)
        current = current.next

    current = linked_b.head
    while current:
        if current.value in values_a:
            common.append(current.value)
        current = current.next

    return common




vowels = LinkedList(values=["a","e","i","o","u"])
letters = LinkedList(values=["a","b","c","d","e"])

common = get_common_items(vowels, letters)
assert common == ["a","e"]

# one liner
common = sorted(set(vowels).intersection(set(letters)))
assert common == ["a","e"]

print("TESTS PASSED")
