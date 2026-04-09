#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:

        # # method 1 binary search: O(log n) time; O(1) space 

        # res = nums[0]
        
        # l, r = 0, len(nums) - 1

        # while l <= r: 

        #     if nums[l] < nums[r]: 

        #         res = min(res, nums[l])

        #         break

        #     m = l + (r - l) // 2

        #     res = min(res, nums[m])

        #     if nums[m] >= nums[r]: # nums[m] in left side, go right, i.e., [m + 1, r]

        #         l = m + 1

        #     else: 

        #         r = m - 1

        # return res


        # method 2 binary search (lower bound): O(log n) time; O(1) space 

        l, r = 0, len(nums) - 1

        while l < r: 

            m = l + (r - l) // 2

            if nums[m] < nums[r]: # Minimum is at m or to the left

                r = m             # Minimum is in [l, m], keep m

            else:                 # Minimum is to the right

                l = m + 1         # Minimum is in [m + 1, r]

        return nums[l]

     
# @lc code=end

