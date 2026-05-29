#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # # method 2 dp (top-down): O(n) time; O(n) space
        # # Optimized version of brute-force / recursive solution

        # memo = {
        #     0: cost[0],
        #     1: cost[1]
        # }

        # def f(n):

        #     if n in memo:

        #         return memo[n]

        #     memo[n] = cost[n] + min(f(n - 1), f(n - 2))

        #     return memo[n]

        # n = len(cost)

        # return min(f(n - 1), f(n - 2))


        # method 3 dp (bottom-up): O(n) time; O(n) space

        n = len(cost)

        dp = [0] * (n + 1)           # dp[i] = minimum cost to reach position i

        dp[0], dp[1] = 0, 0          # Can either start from index 0 or 1 "for free"

        for i in range(2, n + 1):

            dp[i] = min(dp[i - 1] + cost[i - 1],
                        dp[i - 2] + cost[i - 2])

        return dp[n]        


# @lc code=end


# 1. Define f(i) = minimum cost to reach position i.

# 2. To reach position i, it must come from i-1 or i-2.

# 3. Therefore:

#    f(i) = min(
#        f(i-1) + cost[i-1],
#        f(i-2) + cost[i-2]
#    )

# 4. The recursion tree has overlapping subproblems.

# 5. Add memoization.

# 6. Convert memoized recursion to bottom-up DP.