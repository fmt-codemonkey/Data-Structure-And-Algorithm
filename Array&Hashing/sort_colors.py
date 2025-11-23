"""
    8. Sort Colors

    You are given an array `nums` consisting of `n` elements where each element is an integer representing a color: 
        0: represents red
        1: represents white
        2: represents blue

    Your task is to sort the array in-place such that the element of the same color are grouped together and arranged in the order: red(0), white(1) and then blue(2):

    You mush not use any built-in sorting functions to solve this problem.

    Example 1: 
        Input: nums = [1, 0, 1, 2]
        Output: [0, 1, 1, 2]

    Example 2: 
        Input: [2, 1, 0]
        Output: [0, 1, 2]

    Constraints: 
        * 1 <= nums.length <= 300
        * 0 <= nums[i] <= 2

    Follow up: Could you ocme up with a one-pass algorithm using only constant extra space? 
"""

from typing import List

class Solution: 
    def sortColors(self, nums: List[int]) -> None: 
        """
            Sort colors (0, 1, 2) in-place using Dutch National Flag algorithm.

            Approach: Three Pointers (Dutch National Flag Alogrigthm)
                We use three pointers to partition the array into three sections: 
                - [0, ...., left - 1]: All 0's (red)
                - [left, ...., i - 1]: All 1's (white)
                - [right + 1, ...., n - 1]: All 2's (blue)
                - [i, ...., right]: Unsorted elements to process

                We process elements with pointer i: 
                - If nums[i] == 0: Swap with left pointer, move both forward
                - If nums[i] == 1: Already in correct section, move i forward
                - If nums[i] == 2: Swap with right pointer, move right backward

            Args: 
                nums: List ot sort in-place (modifies the orginal list)
            
            Returns: 
                None (modifies nums in-place)

            Time Complexity: O(n)
                We traverse the array once with pointer i

            Space Complexity: O(1)
                Only use three pointer variables, no extra data structure
        """

        left = 0
        i = 0
        right = len(nums) - 1

        # Process elements until i crosses right
        while i <= right:
            if nums[i] == 0:
                # Found a 0, swap with left pointer
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1

            elif nums[i] == 1:
                # Found a 1, it's already in correct position
                i += 1

            else:   # nums[i] == 2
                # Found a 2, swap with right pointer
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
                #  Don't increment i, because we need to check swapped element


def test_solution():
    """
        Test cases for sort colors problems.
    """
    solution = Solution()

    # Example 1: 
    nums1 = [1, 0, 1, 2]
    expected1 = [0, 1, 1, 2]
    solution.sortColors(nums1)
    assert nums1 == expected1, f"Test 1 failed: Expected {expected1}, got {nums1}"
    print(f"Test 1 passed: [1, 0, 1, 2] -> {nums1}")

    # Example 1: 
    nums2 = [2, 1, 0]
    expected2 = [0, 1, 2]
    solution.sortColors(nums2)
    assert nums2 == expected2, f"Test 2 failed: Expected {expected2}, got {nums2}"
    print(f"Test 2 passed: [2, 1, 0] -> {nums2}")


if __name__ == "__main__":
    test_solution()