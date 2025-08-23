from neetcode_250.array_and_hashings.remove_element import Solution

def test_examples():
    s = Solution()

    nums = [1, 1, 2, 3, 4]
    k = s.removeElement(nums, 1)
    assert nums[:k] == [2, 3, 4]

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    k = s.removeElement(nums, 2)
    assert k == 5
    assert sorted(nums[:k]) == sorted([0, 1, 3, 0, 4]) # order not required

def test_edge_cases():
    s = Solution()
    nums = []
    k = s.removeElement(nums, 0)
    assert k == 0
    assert nums[:k] == []

    nums = [1, 2, 3]
    k = s.removeElement(nums, 4)
    assert k == 3
    assert nums[:k] == [1, 2, 3]