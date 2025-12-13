#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        l = 0

        total = 0

        res = float("inf")

        for r in range(len(nums)): 

            total += nums[r] 

            while total >= target: #if total >= target: 

                res = min(r - l + 1, res)

                total -= nums[l]

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
        

# @lc code=end

