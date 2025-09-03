from neetcode_250.array_and_hashings.design_hashset import MyHashSet

def test_examples_sequence():
    hs = MyHashSet()
    hs.add(1)          # set = [1]
    hs.add(2)          # set = [1, 2]
    assert hs.contains(1) is True
    assert hs.contains(3) is False
    hs.add(2)          # duplicates allowed in current version
    assert hs.contains(2) is True
    hs.remove(2)       # removes all copies of 2
    assert hs.contains(2) is False

def test_collisions_same_bucket():
    hs = MyHashSet()
    size = 10000
    keys = [5, 5 + size, 5 + 2*size, 5 + 3*size]  # all collide mod 10000
    for k in keys:
        hs.add(k)
    for k in keys:
        assert hs.contains(k) is True
    hs.remove(5 + size)
    assert hs.contains(5 + size) is False
    assert hs.contains(5) is True
    assert hs.contains(5 + 2*size) is True

def test_duplicates_behavior():
    hs = MyHashSet()
    hs.add(42); hs.add(42); hs.add(42)
    assert hs.contains(42) is True
    hs.remove(42)     # should clear all 42s
    assert hs.contains(42) is False

def test_absent_and_empty_bucket():
    hs = MyHashSet()
    assert hs.contains(999) is False
    hs.remove(999)    # should be a no-op, no exception
    assert hs.contains(999) is False
