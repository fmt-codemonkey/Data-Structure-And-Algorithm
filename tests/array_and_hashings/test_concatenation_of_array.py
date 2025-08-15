from neetcode_250.array_and_hashings.concatenation_of_array import Solution

def test_examples():
    s = Solution()
    assert s.getConcatenation([1, 4, 1, 2]) == [1, 4, 1, 2, 1, 4, 1, 2]
    assert s.getConcatenation([22, 21, 20, 1]) == [22, 21, 20, 1, 22, 21, 20, 1]

def test_edge_cases():
    s = Solution()
    assert s.getConcatenation([5]) == [5, 5]
    assert s.getConcatenation([1000, 999]) == [1000, 999, 1000, 999]
    assert s.getConcatenation([1, 1, 1]) == [1, 1, 1, 1, 1, 1]