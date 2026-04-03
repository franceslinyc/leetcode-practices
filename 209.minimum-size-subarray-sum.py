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
                
                window_sum -= nums[l]            # Careful! Don't forget to decrement 

                l += 1

        return 0 if res == float("inf") else res


# We can use a sliding window and maintain a running sum to track the current window's sum. We expand the right pointer 
# to grow the sum, and once it meets or exceeds the target, shrink from the left to find the minimum length, updating 
# the result along the way. This runs in O(n) time since each element is visited at most twice, with O(1) extra space 
# because we didn't use additional data structures that scale with the input size. 


# Idea: 
# 
# [2 3 1 2 4 3]
# target 7
#  2
#  2 3
#  2 3 1 
#  2 3 1 2 >= target -> update res, decrement window_sum, shrink 
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

