from neetcode_250.array_and_hashings.majority_element import Solution

def test_examples():
    s = Solution()
    assert s.majorityElement([5, 5, 1, 1, 1, 5, 5]) == 5
    assert s.majorityElement([2, 2, 2]) == 2

def test_edge_cases():
    s = Solution()
    assert s.majorityElement([1]) == 1
    assert s.majorityElement([3, 3, 4]) == 3
    assert s.majorityElement([9, 1, 9, 2, 9, 3, 9]) == 9

def test_larget_pattern():
    s = Solution()
    arr = [7] * 600 + [1] * 399 # 999 element, 7 is majority
    assert s.majorityElement(arr) == 7