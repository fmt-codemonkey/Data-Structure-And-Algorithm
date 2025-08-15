"""
Contains Duplication (Easy)
Pattern: Array & Hashing

Idea: 
- Use set to track seen numbers.
- Iterate through nums; if a number is already in set, return True.
- Otherwise, add number to the set and continue.

Time:
- O(n) average - set membership/inserting is O(1) average.

Space: 
- O(n) worst case - all element unique.

Edge cases:
- Empty list -> False
- Single element -> False
- Negatives or large integers
- Duplicates far apart in list

Notes:
- Using a list for 'seen' would cause O(n**2) time due to linear memebership checks.
"""

from typing import List

class Solution:
    def hasDuplication(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        
        return False