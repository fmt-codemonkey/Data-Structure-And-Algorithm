"""
[EASY] Valid Anagram 

Given two string s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a stringt that contains the exact same characters as another string, but the order of the character can be different. 

Example 1:
    Input: s = "racecar", t = "carrace"
    Output: true

Example 2:
    Input: s = "jar", t = "jam"
    Output: false

Constraints:
    s and t consist of lowercase English letters.
"""

class Solution:
    # Apprach 1: Using Bruteforce - Sorting
    '''
    Time Complexity: O(nlog(s) + nlog(t)) = O(nlog(n))
    Space Complexity: O(n)
    '''
    def isAnagram_1(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        if sorted_s == sorted_t:
            return True
        else:
            return False
        
    # Approach 2: Using Hash Map
    '''
    Time Complexity: O(n + m)
    Space Complexity: O(1) Note: Because we have at most 26 different character
    '''
    def isAnagram_2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_s = {}
        count_t = {}

        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)

        if count_s == count_t:
            return True
        else:
            return False
        
    # Approach 3: Using Hash Table (Using Array)
    def isAnagram_3(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True

# Runner
if __name__ == "__main__":
    sol = Solution()
    s_1 = "racecar"
    t_1 = "carrace"
    s_2 = "jar"
    t_2 = "jam"

    print(f"Bruteforce - Sorting: ", sol.isAnagram_1(s_1, t_1))
    print(f"Bruteforce - Sorting: " ,sol.isAnagram_1(s_2, t_2))

    print(f"Hash Map: ", sol.isAnagram_1(s_1, t_1))
    print(f"Hash Map: ", sol.isAnagram_2(s_2, t_2))

    print(f"Hash Table (Using Array): ", sol.isAnagram_3(s_1, t_1))
    print(f"Hash Table (Using Array): ", sol.isAnagram_3(s_2, t_2))