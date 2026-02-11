#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
from typing import List
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        this_dict = {}

        for i, n in enumerate(nums): 
            
            diff = target - n 

            if diff in this_dict: 

                return [i, this_dict[diff]]
            
            this_dict[n] = i      # Careful here! 

        # this_dict = {}

        # for i in range(len(nums)): 

        #     diff = target - nums[i]

        #     if diff in this_dict: 

        #         return [i, this_dict[diff]]
            
        #     this_dict[nums[i]] = i


# @lc code=end

