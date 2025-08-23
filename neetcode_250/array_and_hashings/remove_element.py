"""
Remove Element (Easy)
Pattern: Two Pointer / In-place Array

Idea:
- We need to "filter out" all occurrences of val in-place.
- Use a write pointer (k) to mark the position of the next valid element. 
- Iterate over nums with a  read pointer:
    - If nums[i] != val, copy nums[i] into nums[k] and increment k.
- After the loop, k is the count of valid elements.
- the firest k positions of nums are now val-free.

Time: 
- O(n), we scan the array once.

Space:
- O(1), in-place.

Edge cases:
- Empty array -> return 0
- All elements equal to val -> return 0
- No elements equal to val -> return len(nums)
"""

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0 # write pointer
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k
