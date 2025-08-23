"""
Majority Element (Easy)
Pattern: Array & Hashing

Idea: 
- Count the frequency of each number using a hash map (dict).
- The majority element must appear > n/2 times, so return the one with the highest count.

Time: 
- O(n) to build counts and scan

Space:
- O(n) in worst case (all number are unique)

Edge Cases:
- n=1 -> return that element
"""

from typing import List
from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        n = len(nums)

        for num in nums: 
            counts[num] += 1
            if counts[num] > n // 2:
                return num
        
        return -1