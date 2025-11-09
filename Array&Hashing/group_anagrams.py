"""
    5. Given an array of string `strs`, group all anagrams together into sublists. You may return the output in any order. 

    An anagram is a string that contains the exact same characters as another stirng, but the order of the characters can be different. 


    Example 1: 
        Input: strs = ["act", "pots", "tops", "cat", "stop", "hat"]
        Output: [["hat"], ["act, "cat"], ["stop", "pots", "tops"]]

    Example 2: 
        Input: strs = ["x"]
        Output: [["x"]]

    Example 3: 
        Input: strs = [""]
        Output: [[""]]

        
    Constraints:
    * 1 <= strs.length <= 1000.
    * 0 <= strs[i].length <= 1000.
    * strs[i] is made up of lowercase English letters.
"""

from typing import List
from collections import defaultdict

class Solution: 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
            Group all anagrams together using a hash map. 

            Approach: 
                I will use a hash map to group anagrams. For each word, I will create a signature  by counting the frequency of each character (a - z). Words with the same character counts are anagrams. I will store each word in the hash map under its signature, then return all the groups. 

            Args: 
                strs: List of strings to group

            Returns: 
                List of Lists, where each inner list contains anagrams

            
            * Time Complexity: O(n * k)
                We iterate through n strings, and for each string, we iterate thorough k characters to count them

            * Space Complexity: O(n * k)
                We store all n strings in the hash map, each of length k
        """

        result = defaultdict(list)

        for word in strs: 
            # i. Create a signature
            count = [0] * 26
            
            for char in word: 
                index = ord(char) - ord('a')
                count[index] += 1

            signature = tuple(count)

            # ii. Add word to the group 
            result[signature].append(word)

        return list(result.values())


def test_solution():
    """
        Test cases for group anagrams problems. 
    """
    solution = Solution()

    # Example 1 
    strs1 =  ["act", "pots", "tops", "cat", "stop", "hat"]
    expected1 = [['act', 'cat'], ['pots', 'tops', 'stop'], ['hat']]
    result1 = solution.groupAnagrams(strs1)
    assert result1 == expected1, f"Test 1 Failed: Expected {expected1}, got {result1}"
    print(f"Test 1 Passed: {strs1} -> {result1}")

    # Example 2 
    strs2 = ["x"]
    expected2 = [["x"]]
    result2 = solution.groupAnagrams(strs2)
    assert result2 == expected2, f"Test 2 Failed: Expected {expected2}, gor {result2}"
    print(f"Test 2 Passed: {strs2} -> {result2}")

    # Example 3
    strs3 = [""]
    expected3 = [[""]]
    result3 = solution.groupAnagrams(strs3)
    assert result3 == expected3, f"Test 3 Failed: Expected {expected3}, gor {result3}"
    print(f"Test 3 Passed: {strs3} -> {result3}")


if __name__ == "__main__":
    test_solution()