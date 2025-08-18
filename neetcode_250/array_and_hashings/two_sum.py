"""
Two Sum (Easy)
Pattern: Array & Hashing

Idea: 
- For each number, we need to check if (target - num) has been seen before.
- Use a hash map (dict) to store value -> index as we iterate. 
- If complement is found, return [stored_index, current_index]

Time: 
- O(n) - single pass through nums. 
Space:
- O(n) - hash map stores up to n elements. 

Edge cases:
- Duplicate numbers (e.g., [5, 5], target=10)
- Negative numbers or large values
"""

from typing import List, Dict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen: Dict[int, int] = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in seen:
                return [seen[diff], i]
            seen[n] = i

        return []  