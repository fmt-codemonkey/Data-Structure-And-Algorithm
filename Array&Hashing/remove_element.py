"""
    6. You are given an integer array `nums` and an integer `val`. Your task is to remove all occurrences of `val` from `nums` in-place.

    After removing all occurrences of `val`. return the number of remaining elements, say `k`. such that the first `k` element of `nums` do not contain `val`.

    Note: 
        - The order of the elements which are not equal to `val` does not matter. 
        - It is not necessary to consider elements beyond the first `k` positions of the array. 
        - To be accepted, the first `k` elements of `nums` must contain only elements not equal to `val`. 

    Return `k` as the final result.


    Example 1: 
        Input: nums = [1, 1, 2, 3, 4], val = 1
        Output: [2, 3, 4]
        Explanation: You should return `k = 3` as we have `3` elements which are not equal to `val = 1`. 

    Example 2: 
        Input: nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2
        Output: [0, 1, 3, 0, 4]
        Explanation: You should return `k = 5` as we have 5 elements which are not equal to `val = 2`.

        
    Constraints: 
        * 0 <= nums.length <= 100
        * 0 <= nums[i] <= 50
        * 0 <= val <= 100
"""

from typing import List

class Solution: 
    def removeElement(self, nums: List[int], val: int) -> int:
        """
            Remove all occurrences of val from nums in-place and return the new length.

            Approach: Two pointers
                I will use two pointers - one to iterate through the array (i) and one to track the position for the next valid element (k).

                When we find an element that is NOT equal to val, we place it at position k and increment k, Elements equal to val are skipped. 

                At the end, k represents the count of valid elements, and the first k positions of nums contain only elements not equal to val.

            Args:
                nums: List of integers to modify in-place
                val: The value to remove

            Returns: 
                k: The number of elements not equal to val

            
            * Time Complexity: O(n)
                We iterate through the array once

            * Space Complexity: O(1)
                We only use two pointer variables, no extra space for data structures
        """

        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k
    

def test_solution():
    """
        Test cases for remove element problem.
    """
    solution = Solution()

    # Exmaple 1
    nums1 = [1, 1, 2, 3, 4]
    val1 = 1
    expected1 = 3
    result1 = solution.removeElement(nums1, val1)
    assert result1 == expected1, f"Test 1 Failed: Expected k={expected1}, got k={result1}"
    print(f"Test 1 Passed: nums={nums1} without vals={val1} -> {result1}")

    # Exmaple 2
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    expected2 = 5
    result2 = solution.removeElement(nums1, val1)
    assert result2 == expected2, f"Test 1 Failed: Expected k={expected2}, got k={result2}"
    print(f"Test 2 Passed: nums={nums2} without vals={val2} -> {result2}")


if __name__ == "__main__":
    test_solution()