from neetcode_250.array_and_hashings.valid_anagram import Solution

def test_examples():
    s = Solution()
    assert s.isAnagram("racecar", "carrace") is True
    assert s.isAnagram("jar", "jam") is False

def test_edge_cases():
    s = Solution()
    assert s.isAnagram("", "") is True
    assert s.isAnagram("a", "a") is True
    assert s.isAnagram("a", "b") is False
    assert s.isAnagram("anagram", "nagaram") is True
    assert s.isAnagram("rat", "car") is False