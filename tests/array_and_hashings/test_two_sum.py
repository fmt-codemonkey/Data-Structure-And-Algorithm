from neetcode_250.array_and_hashings.two_sum import Solution

def test_examples():
    s = Solution()
    assert s.twoSum([3, 4, 5, 6], 7) == [0, 1]
    assert s.twoSum([4, 5, 6], 10) == [0, 2]
    assert s.twoSum([5, 5], 10) == [0, 1]

def test_edge_cases():
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert s.twoSum([-1, -2, -3, -4, -5], -8) == [2, 4]
    assert s.twoSum([0, 4, 3, 0], 0) == [0, 3]