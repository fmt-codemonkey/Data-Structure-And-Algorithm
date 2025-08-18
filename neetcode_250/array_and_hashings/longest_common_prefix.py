"""
Longest Common Prefix (Easy)
Pattern: String manipulation

Idea:
- The longest common prefix must be a prefix of the shortest string.
- Approach:
    1. Take the first string as candidate prefix.
    2. Compare with each subsequent string, shrink prefix until match. 
    3. If prefix becomes empty -> return ""

Time: 
- O(n * m) where n = number of strings, m = min string length.
 (We compare character across strings.)

Space: 
- O(1) extra

Edge cases:
- Single string in input -> return that string.
- One or more empty string -> return "".
- No commpon prefix -> return "".
"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]
        for s in strs[1: ]:
            # Shrink prefix until it's a prefix of s
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
        
        return prefix