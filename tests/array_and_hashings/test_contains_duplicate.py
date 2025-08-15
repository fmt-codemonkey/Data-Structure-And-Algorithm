from neetcode_250.array_and_hashings.contains_duplicate import Solution

def test_examples():
    s = Solution()
    assert s.hasDuplication([1, 2, 3, 1]) is True
    assert s.hasDuplication([1, 2, 3, 4]) is False

def test_edge_cases():
    s = Solution()
    assert s.hasDuplication([]) is False
    assert s.hasDuplication([1]) is False
    assert s.hasDuplication([0, 0]) is True
    assert s.hasDuplication([-1, -1]) is True

def test_large_case():
    s = Solution()
    nums = list(range(10_000))
    assert s.hasDuplication(nums) is False
    
    nums.append(500)
    assert s.hasDuplication(nums) is True