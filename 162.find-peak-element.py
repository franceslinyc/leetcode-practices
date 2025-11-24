#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1

        while l <= r: 

            m = l + ((r - l) // 2) # m = (l + r) // 2

            if m > 0 and nums[m] < nums[m - 1]: 

                r = m - 1

            elif m < len(nums) - 1 and nums[m] < nums[m + 1]: 

                l = m + 1

            else: 

                return m
        
# @lc code=end

