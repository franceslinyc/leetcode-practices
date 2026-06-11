#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # method 1: recursive binary search: O(log n) time; O(log n) space 

        # method 2: iterative binary search: O(log n) time; O(1) space

        l, r = 0, len(nums) - 1

        while l <= r: # Inclusive range [l, r]; Must check when l == r (last element)

            m = l + ((r - l) // 2) # Avoid overflow, compared to m = (l + r) // 2

            if nums[m] == target: 

                return m
            
            elif nums[m] < target: # Too small, search right, i.e., [m + 1, r] 

                l = m + 1
            
            else:                  # Too big, search left, i.e., [l, m - 1]

                r = m - 1
        
        return -1
    

        # TODO
        # method 3 upper bound: O(log n) time; O(1) space 
        # method 4 lower bound: O(log n) time; O(1) space
    

# @lc code=end

