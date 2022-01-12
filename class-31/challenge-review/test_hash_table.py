from hash_table import HashTable


def test_create():
    ht = HashTable()

    assert ht
    assert ht.buckets


def test_hash():
    ht = HashTable()
    assert ht.hash("cat") == ht.hash("act")
    assert ht.hash("cab") != ht.hash("act")


def test_add_nosy():
    ht = HashTable()
    cat_hash = ht.hash("cat")
    ht.add("cat", "Cleo")
    assert ht.buckets[cat_hash].head.value == ("cat", "Cleo")


def test_add_again():
    ht = HashTable()
    cat_hash = ht.hash("cat")
    ht.add("cat", "Cleo")
    ht.add("cat", "Garfield")
    assert ht.buckets[cat_hash].head.value == ("cat", "Garfield")
