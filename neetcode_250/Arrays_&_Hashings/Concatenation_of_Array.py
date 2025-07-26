"""
[EASY] Concatenation of Array

You are given an integer array nums of length n. Create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specially, ans is the concatenation of two nums arrays. 

Return the array ans.

Example 1:
    Input: nums = [1, 4, 1, 3]
    Output: ans = [1, 4, 1, 2, 1, 4, 1, 2]

Example 2: 
    Input: nums = [22, 21, 20, 1]
    Output: ans = [22, 21, 20, 1, 22, 21, 20, 1]  
"""


from typing import List

class Solution:
    # Approach 1: Using 2 for loop
    '''
    Time Complexity: O(n)
    Space Complexity: O(n)
    '''
    def getConcatenation_1(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            for i in range(len(nums)):
                ans.append(nums[i])
        
        return ans
    
    # Approach 2: Using 1 for loop
    '''
    Time Complexity: O(n)
    Space Complexity: O(n)
    '''
    def getConcatenation_2(self, nums: List[int]) -> List[int]:
        nums_length = len(nums)
        ans = [0] * (2 * nums_length)
        for i in range(nums_length):
            ans[i] = nums[i]
            ans[i + nums_length] = nums[i]

        return ans
    
    # Approach3: Using list concatenation
    '''
    Time Complexity: O(n)
    Space Complexity: O(n)
    '''
    def getConcatenation_3(self, nums: List[int]) -> List[int]:
        return nums + nums

    
# Runner
if __name__ == "__main__":
    sol = Solution()
    nums = [1, 4, 1, 2]

    print(sol.getConcatenation_1(nums), ": Using 2 Loops")
    print(sol.getConcatenation_2(nums), ": Using 1 Loops")
    print(sol.getConcatenation_3(nums), ": Using list concatenation")
