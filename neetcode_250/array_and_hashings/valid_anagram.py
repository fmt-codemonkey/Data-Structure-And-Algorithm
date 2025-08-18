"""
Valid Anagram (Easy)
Pattern: Array & Hashing

Idea: 
- Two string are anagrams if they have identical character frequencies.
- If lengths differ -> immediately False.
- Count chars in both strings (using dict or Counter) and compare.

Time: 
- O(n + m) where n = len(s) and m = len(t)
Space: 
- O(1) techincally (since only 26 lowercase letters possible)
- But O(n) if counting distinct characters more generally

Edge cases:
- Different lengths -> False
- Empty strings -> True
Repeated characters
"""

from typing import Dict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_hash: Dict[str, int] = {}
        t_hash: Dict[str, int] = {}

        for i in range(len(s)):
            s_hash[s[i]] = 1 + s_hash.get(s[i], 1)
            t_hash[t[i]] = 1 + t_hash.get(t[i], 1)

        return s_hash == t_hash