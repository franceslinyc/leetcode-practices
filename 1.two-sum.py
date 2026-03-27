#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
from typing import List
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # method 2: sorting: time O(n log n); space O(n)
        
        # method 3: hash map: time O(n); space O(n)
        
        this_dict = {}

        for i, num in enumerate(nums): 
            
            diff = target - num 

            if diff in this_dict: 

                return [this_dict[diff], i]     # Careful! Better to have previous index first, current index second
            
            this_dict[num] = i                  # Careful here! 

        # this_dict = {}

        # for i in range(len(nums)): 

        #     diff = target - nums[i]

        #     if diff in this_dict: 

        #         return [i, this_dict[diff]]
            
        #     this_dict[nums[i]] = i


# Related to LC 167, 15


# @lc code=end

