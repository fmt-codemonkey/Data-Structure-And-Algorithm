"""
    1. Concatenation of Array

    
    You are given an integer array `nums` of len `n`. Create an array `ans` of lenght `2n` where `ans[i] == nums[i]` and `ans[i+n] == nums[i]` for `0 <= i < n` (0-indexed).

    Specially, `ans` is the concatenation of two `nums` arrays.

    Return the array `ans`.

    
    Example 1: 
        Input: nums = [1, 4, 1, 2]
        Output: [1, 4, 1, 4, 1, 4, 1, 2]

    Example 2: 
        Input: nums = [22, 21, 20, 1]
        Output: [22, 21, 20, 1, 22, 21, 20, 1]

        
    Constraints: 
        * 1 <= nums.length <= 1000
        * 1 <= nums[i] <= 1000         
"""

from typing import List

class Solution: 
    def getConcatenation(self, nums: List[int]) -> List[int]:
        """
            Concatenate the array with itself by appending all elements again.

            Apporach 1: 
                I will extend the array with itself. Python allow us to concatenate the list using the + operator.

            Args: 
                nums: The input array to concatenate with itself

            Returns: 
                Array that is nums concatenated with itself

            
            * Time Complexity: O(n) 
                We iterate through the n element once to copy them

            * Space Complexity: O(n)
                We create a new array of 2n and we ignore the constants
        """

        return nums + nums
    

def test_solution():
    """
    Test cases for array concatenation.
    """
    solution = Solution()

    # Example 1:
    nums1 = [1, 4, 1, 2]
    expected1 = [1, 4, 1, 2, 1, 4, 1, 2]
    result1 = solution.getConcatenation(nums1)
    assert result1 == expected1, f"Test 1 Failed: Expected {expected1}, got {result1}"
    print(f"Test 1 Passed: {nums1} -> {result1}")

    # Example 2  
    nums2 = [22, 21, 20, 1]
    expected2 = [22, 21, 20, 1, 22, 21, 20, 1]
    result2 = solution.getConcatenation(nums2)
    assert result2 == expected2, f" Test 2 failed: Expected {expected2}, got {result2}"
    print(f"Test 2 Passed: {nums2} -> {expected2}")


if __name__ == "__main__":
    test_solution()