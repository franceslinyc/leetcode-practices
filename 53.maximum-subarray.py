#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # # method 6 Kadane's Algorithm via NeetCode: O(N) time; O(1) space

        # max_sum = nums[0]

        # current_sum = 0 

        # for num in nums: 

        #     if current_sum < 0:    

        #         current_sum = 0    # Restart subarray

        #     current_sum += num     # Always extend
            
        #     max_sum = max(max_sum, current_sum)

        # return max_sum


        # method 6 variaion Kadane's Algorithm via Coding Interview Book: O(N) time; O(1) space

        max_sum = nums[0]

        current_sum = 0

        for num in nums: 

            current_sum = max(current_sum + num, num) # Either prev sum value + current num or current num

            max_sum = max(max_sum, current_sum)

        return max_sum


        # # method 7 dp O(N) time; O(N) space

        # if len(nums) == 0: 

        #     return 0

        # max_sum = nums[0]

        # dp = [0] * len(nums)

        # dp[0] = nums[0]

        # for i in range(1, len(nums)): 

        #     dp[i] = max(dp[i - 1] + nums[i], nums[i])     # Either prev sum value + current num or current num

        #     max_sum = max(max_sum, dp[i])

        # return max_sum


        # # method 8 dp (space optimized): O(N) time; O(1) space

        # if len(nums) == 0: 

        #     return 0 

        # max_sum = nums[0]

        # current_sum = nums[0]

        # for i in range(1, len(nums)): 

        #     current_sum = max(current_sum + nums[i], nums[i])

        #     max_sum = max(max_sum, current_sum)

        # return max_sum


# @lc code=end

