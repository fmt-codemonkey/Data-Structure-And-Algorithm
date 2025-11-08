"""
    2. Contains Duplication

    Given an integer array `nums`, return `true` if any value appears more than once in the array, otherwise return `false`.

    Example 1: 
        Input: nums = [1, 2, 3, 3]
        Output: true

    Exmaple 2: 
        Input: nums = [1, 2, 3, 4]
        Output: false
"""

from typing import List

class Solution: 
    def hasDuplication(self, nums: List[int]) -> bool: 
        """
            Check if any value appears more than once in the array.

            Approach 1: 
                Using a set to track seen element

                We iterate through the array and use a set to keep a track of elements we've already seen. If we encounter an element that's aleady in the set, then we have found a duplicate and return True. If we complete the iteration without finding duplicates, return False.

            Args: 
                nums: The input array to check for duplicates

            Returns: 
                True if the element appears more than once, otherwise False

            * Time Complexity: O(n)
                We iterate through all the element once, and set loopup/insert is O(1)

            * Space Complexity: O(n)
                In the worst case (no duplication), we store all n elements in the set

        """
        seen = set()

        for n in nums: 
            if n in seen: 
                return True
            
            seen.add(n)
        
        return False
    

def test_solution():
    """
        Test cases for duplication detection.
    """
    solution = Solution()

    # Exmaple 1:
    nums1 = [1, 2, 3, 3]
    expected1 = True
    result1 = solution.hasDuplication(nums1)
    assert result1 == expected1, f"Test 1 Failed: Expected {expected1}, got {result1}"
    print(f"Test 1 Passed: {nums1} -> {result1}")

    # Example 2: 
    nums2 = [1, 2, 3, 4]
    expected2 = False
    result2 = solution.hasDuplication(nums2)
    assert result2 == expected2, f"Test 2 Failed: Expected {expected2}, got {result2}"
    print(f"Test 2 Passed: {nums2} -> {result2}")


if __name__ == "__main__": 
    test_solution()