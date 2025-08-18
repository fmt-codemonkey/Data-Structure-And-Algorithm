"""
Concatenation of Array (Easy)
Pattern: Array building

Idea: 
- Return the input twice in order: nums + nums (or nums * 2).

Time:
- O(n) because Python must copy 'nums' twice into a new list.

Space:
- O(n) for output (2n length).

Edge cases:
- n = 1 (eg., [5] -> [5, 5])
- Duplicates already handled naturally.

Notes: 
- This is a straightforward array contruction problem. No special DS needed.
"""

from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Alternatively, return nums * 2 
        return nums + nums