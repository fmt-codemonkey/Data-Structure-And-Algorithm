"""
    7. Majority Element

    Given an array `nums` of size `n`, return the majority element.

    The majority element is the element that appears more than `[n/2]` times in the array. You may assume that the majority element always exists in the array. 

    Example 1: 
        Input: nums = [5, 5, 1, 1, 1, 5, 5]
        Output: 5

    Example 2: 
        Input: nums = [2, 2, 2]
        Output: 2

    Constraints: 
        * 1 <= nums.length <= 50,000
        * -1,000,000,000 <= nums[i] <= 1,000,000,000

    Follow-up: 
        Could you sovle the problme in linear time and in O(1) space? 
"""

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int: 
        """
            Finding the majority element using Boyer-Moore Voting Alogrithm.

            Approach: Boyer-Moore Voting Algorithm
                The key insights is that if we cancel out each occurence of element with all the other elements that are different from it, the majority element will still remain. 

                We maintain a candidate and a count: 
                - If count is 0, we pick the current element as candidate
                - If current element equals candidate, increment count
                - If current element differes from candidate, decrement count

                The candidate at the end will be the majority element. 

            Args: 
                nums: List of integers

            Returns:
                The majority element (appears more that n/2 times)

            * Time Complexity: O(n)
                We itegrate through the array once
            
            * Space Complexity: O(1)
                We only use two variables: candidate and count
        """

        candidate = 0
        count = 0

        for num in nums: 
            # If count = 0, pick current element as new candidate
            if count == 0: 
                candidate = num

            # If other element matches candidate, increment count otherwise decrement count
            if num == candidate: 
                count += 1
            else: 
                count -= 1

        return candidate
    

def test_solution():
    """
        Test cases for majority element problem.
    """
    solution = Solution()

    # Example 1: 
    nums1 = [5, 5, 1, 1, 1, 5, 5]
    expected1 = 5
    result1 = solution.majorityElement(nums1)
    assert result1 == expected1, f"Test 1 Failed: Expected {expected1}, got {result1}"
    print(f"Test 1 Passed: nums={nums1} -> {result1}")

    # Example 2 
    nums2 = [2, 2, 2]
    expected2 = 2
    result2 = solution.majorityElement(nums2)
    assert result2 == expected2, f"Test 2 Failed: Expected {expected2}, got {result2}"
    print(f"Test 2 Passed: nums={nums2} -> {result2}")


if __name__ == "__main__":
    test_solution()