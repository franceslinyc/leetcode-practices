#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
from typing import List
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        this_map = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in this_map: 
                return [i, this_map[diff]]
            this_map[n] = i

# @lc code=end

