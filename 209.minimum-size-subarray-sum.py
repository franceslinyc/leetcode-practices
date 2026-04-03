#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        # method: sliding window: O(n) time; O(1) extra space

        res = float("inf")

        window_sum = 0

        # Similar to LC 3, 76

        l = 0 

        for r in range(len(nums)): 

            window_sum += nums[r]

            while window_sum >= target: 

                res = min(res, r - l + 1)
                
                window_sum -= nums[l]

                l += 1

        return 0 if res == float("inf") else res


# [2 3 1 2 4 3]
# target 7
#  2
#  2 3
#  2 3 1 
#  2 3 1 2 >= target -> update res, decrement total, shrink 
#  3 1 2 
#  3 1 2 4 >= target 
#  1 2 4   >= target   
#  2 4
#  2 3 4   >= target
#  3 4     >= target

# [1 1 1 1 1 1 1 1]
# target 11
# never get to update res, i.e., res = float("inf"), return 0        


# @lc code=end

