"""
[EASY] Contains Duplicate

Given an integer array nums, return true if any value appears more than once in the array, otherwise return false. 

Example 1:
    Input: nums = [1, 2, 3, 3]    
    Output: true

Example 2:
   Input: nums = [1, 2, 3, 4]
   Output: false 
"""

from typing import List

class Solution:
    # Approach 1: Bruteforce
    '''
    Time Complexity: O(n*2)
    Space Complexity: O(1)
    '''
    def hasDuplication_1(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True   
        return False
    
    
    # Approach 2: Sorting
    '''
    Time Complexity: O(nlogn) -> sort is expensive
    Space Complexity: O(1)
    '''
    def hasDuplication_2(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
    
    
    # Apporach 3: Hash Set
    '''
    Time Complexity: O(n)
    Space Complexity: O(n)
    '''
    def hasDuplication_3(self, nums: List[int]) -> bool:
        hash_set = set()
        for num in nums:
            if num in hash_set:
                return True 
            hash_set.add(num)
        return False
    

    # Apprach 4: Hash Set Length
    '''
    Time Complexity: O(n)
    Space Complexity: O(n)
    '''
    def hasDuplication_4(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)

    

# Runner
if __name__ == "__main__":
    sol = Solution()
    nums_one = [1, 2, 3, 3]
    nums_two = [1, 2, 3, 4]

    print(f"BruteForce: {nums_one}: ", sol.hasDuplication_1(nums_one))
    print(f"BruteForce: {nums_two}:", sol.hasDuplication_1(nums_two))

    print(f"Sorting: {nums_one}: ", sol.hasDuplication_2(nums_one))
    print(f"Sorting: {nums_two}: ", sol.hasDuplication_2(nums_two))

    print(f"Hash Set: {nums_one}", sol.hasDuplication_3(nums_one))
    print(f"Hash Set: {nums_two}", sol.hasDuplication_3(nums_two))

    print(f"Hash Set Length: {nums_one}", sol.hasDuplication_4(nums_one))
    print(f"Hash Set Length: {nums_two}", sol.hasDuplication_4(nums_two))
