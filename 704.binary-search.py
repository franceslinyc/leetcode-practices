#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l <= r: 

            m = l + ((r - l) // 2) # m = (l + r) // 2

            if nums[m] == target: 

                return m
            
            elif nums[m] < target: 

                l = m + 1
            
            else: 

                r = m - 1
        
        return -1
    
        # method 3 upper bound 
        # method 4 lower bound
    
# @lc code=end

