"""
    3. Valid Anagram

    Given two string `s` and `t`, return `true` if the two strings are anagrams of each other, otherwise return `false`. 

    An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

    Example 1: 
        Input: s = "racecar", t = "carrace"
        Output: true

    Example 2: 
        Input: s = "jar", t = "jam"
        Output: false

    Constraints: 
        * `s` and `t` consist of lowercase English letters. 
"""

from typing import List

class Solution: 
    def isAnagram(self, s: str, t: str) -> bool: 
        """
            Check if two strings are anagrams of each other.

            Approach 1: 
                I will create two hashmap to store the each character of s and T, and compare them.

            Args: 
                s: First string
                t: Second string

            Returns: 
                True if the strings are anagram, False otherwise.

            * Time Complexity: O(n + m)
                We interate through the loop only 1 times to check every character of string

            * Space Complexity: O(1)
                We use the two hash maps to store character counts, Since the problem states that strings consist of lowercase English letters only, each hash map can store at most 26 characters, which is a constant.
        """

        if len(s) != len(t):
            return False
    
        countS = {}
        countT = {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT

def test_solution():
    """
        Test case for valid anagaram
    """
    solution = Solution()

    # Example 1: 
    s1 = "racecar"
    t1 = "carrace"
    expected1 = True
    result1 = solution.isAnagram(s1, t1)
    assert result1 == expected1, f"Test 1 Failed: Expected {expected1}, got {result1}"
    print(f"Test 1 Passed: {s1}, {t1} -> {result1}")

    # Example 2:
    s2 = "jar"
    t2 = "jam"
    expected2 = False
    result2 = solution.isAnagram(s2, t2)
    assert result2 == expected2, f"Test 2 Failed: Expected {expected2}, got {result2}"
    print(f"Test 2 Passed: {s2}, {t2} -> {result2}")


if __name__ == "__main__":
    test_solution()