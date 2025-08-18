from neetcode_250.array_and_hashings.longest_common_prefix import Solution

def test_examples():
    s = Solution()  
    assert s.longestCommonPrefix(["bat", "bag", "bank", "band"]) == "ba"
    assert s.longestCommonPrefix(["dance", "dag", "danger", "damage"]) == "da"
    assert s.longestCommonPrefix(["neet", "feet"]) == ""

def test_edge_cases():
    s = Solution()
    assert s.longestCommonPrefix(["flower"]) == "flower"
    assert s.longestCommonPrefix(["", "abc"]) == ""
    assert s.longestCommonPrefix(["abc", ""]) == ""
    assert s.longestCommonPrefix([]) == ""
    assert s.longestCommonPrefix(["dog", "racecar", "car"]) == ""