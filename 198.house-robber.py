#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:

        # # method 2 dp (top-down): O(n) time; O(n) space

        # if not nums:

        #      return 0

        # if len(nums) == 1:

        #     return nums[0]
        
        # memo = {
        #     0: nums[0],
        #     1: max(nums[0], nums[1])
        # }

        # def f(n):

        #     if n in memo:

        #         return memo[n]

        #     memo[n] = max(f(n - 1), nums[n] + f(n - 2))

        #     return memo[n]

        # return f(len(nums) - 1)


        # method 3 dp (bottom-up): O(n) time; O(n) space

        if not nums:

            return 0

        if len(nums) == 1:

            return nums[0]

        dp = [0] * len(nums) # dp[i] = best total achievable amount of money considering houses up through i

        dp[0] = nums[0]

        dp[1] = max(nums[0], nums[1]) 

        for i in range(2, len(nums)):

            dp[i] = max(dp[i - 1],             # Do not rob: Carry forward previous best 
                        nums[i] + dp[i - 2])   # Rob i: Current + best up through i-2; i-2 because robbing i locks out i-1

        return dp[-1]


# @lc code=end


#                0 1 2 3
# Input: nums = [1,2,3,1]
# Output: 4

# DP[i]: best total achievable amount of money considering houses up through i

# DP(0) = nums[0] = 1
# DP(1) = max(nums[0], = max(1, # Do not rob House 1
#             nums[1])       2) # Rob House 1
# DP(2) = max(DP(1),            # Do not rob House 2
#             3 + DP(0))        # Rob House 2
# DP(3) = max(DP(2),            # Do not rob House 3
#             1 + DP(1))        # Rob House 3