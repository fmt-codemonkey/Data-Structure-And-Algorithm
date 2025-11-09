"""
    4. Given an array of integeres `nums` and an integer `target`, return the indices `i` and `j` such that `nums[i] + nums[j] == target` and `i != j`.

    You may assume that every input has exactly one pair of indices `i` and `j` that satisfy the condition. 

    Return the answer with the smaller index first. 

    
    Example 1: 
        Input: nums = [3, 4, 5, 6], target = 7
        Output: [0, 1]

    Example 2: 
        Input: nums = [4, 5, 6], target = 10
        Output: [0, 2]

    Example 3: 
        Input: nums = [5, 5], target = 10
        Output: [0, 1]

    
    Constraints:
        * 2 <= nums.length <= 1000
        * -10,000,000 <= nums[i] <= 10,000,000
        * -10,000,000 <= target <= 10,000,000
"""

from typing import List

class Solution: 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
            Find the two indices where the sum of two values is equal to target.

            Approach: Using hash map
                We iterate throught the array, for each number we calculate what value we need to reach the targt (complement = target - num). We check if this complement exist in our hash map and if it does, we found our pair, if not, we store the currenct number and its index in our hashmap for future loopups. 

            Args: 
                nums: List fo integers to search through
                target: The target sum, we are looking for
            
            Returns: 
                List containing two indices [i, j], where nums[i] + nums[j] == target


            * Time Complexity: O(n)
                We iterate throught the array once, and hash map lookup/insert is O(1)

            * Space Complexity: O(n)
                In the worst case, we store all n elements in the hashmap before finding the pair. 
        """

        # Hash Map to store: {value: index}
        seen = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in seen: 
                return [seen[diff], i]
            
            seen[n] = i

        return []
    

def test_solution():
    """
        Test cases for two sum problem
    """
    solution = Solution()

    # Example 1 
    nums1 = [3, 4, 5, 6]
    target1 = 7
    expected1 = [0, 1]
    result1 = solution.twoSum(nums1, target1)
    assert result1 == expected1, f"Test 1 Failed: Expected {expected1}, got {result1}"
    print(f"Test 1 passed: {nums1}, {target1} -> {result1}")

    # Example 2
    nums2 = [4, 5, 6]
    target2 = 10
    expected2 = [0, 2]
    result2 = solution.twoSum(nums2, target2)
    assert result2 == expected2, f"Test 2 Failed: Expected {expected2}, got {result2}"
    print(f"Test 2 passed: {nums2}, {target2} -> {result2}")

    # Example 3 
    nums3 = [5, 5]
    target3 = 10
    expected3 = [0, 1]
    result3 = solution.twoSum(nums3, target3)
    assert result3 == expected3, f"Test 3 Failed: Expected {expected3}, got {result3}"
    print(f"Test 3 passed: {nums3}, {target3} -> {result3}")


if __name__ == "__main__":
    test_solution()