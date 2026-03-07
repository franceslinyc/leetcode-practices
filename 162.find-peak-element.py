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

            m = (l + r) // 2 # Better use m = l + ((r - l) // 2) to prevent overflow

            if m < len(nums) - 1 and nums[m] < nums[m + 1]: 

                l = m + 1    # Search right

            elif m > 0 and nums[m] < nums[m - 1]: 

                r = m - 1    # Search left

            else: 

                return m


# e.g., 
# [1, 2, 3, 4]    -> Just need to make sure not going out of boundary
# [4, 3, 2, 1]    -> Same with this one
# [1, 2, 3, 4, 1]
#        m  m+1   -> Search right
# [1, 4, 3, 2, 1]
#     m-1m        -> Search left

        
# @lc code=end

