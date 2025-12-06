#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:

        # method 1 dp (bottom-up)
        if n <= 2: 
            return n
        
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2

        for i in range(3, n + 1): 
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

        # method 2 dp (space optimized)

        # method 3 math
        
# @lc code=end

