#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:

        # # method 1 brute-force / recursive: O(2^n) time; O(n) space 

        # if n <= 2: 

        #     return n

        # return self.climbStairs(n - 1) + self.climbStairs(n - 2)


        # # method 2 dp (top-down): O(n) time; O(n) space
        # # Optimized version of brute-force / recursive solution

        # memo = {1:1, 2:2}

        # def f(n): 

        #     if n in memo: 

        #         return memo[n]

        #     memo[n] = f(n - 1) + f(n - 2)

        #     return memo[n]

        # return f(n)


        # method 3 dp (bottom-up): O(n) time; O(n) space

        if n <= 2: 

            return n

        dp = [0] * (n + 1)           # dp[i] = number of ways to reach position i

        dp[1], dp[2] = 1, 2          # base cases; dp[0] = 0 does not make sense

        for i in range(3, n + 1):    # Start at 3 because we already know dp[1], dp[2]

            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


        # # method 4 dp (space optimized): O(n) time; O(1) space

        # if n <= 2: 

        #     return n

        # two_step_back = 1         # <- dp[1]

        # one_step_back = 2         # <- dp[2]

        # for i in range(3, n + 1): 

        #     current = one_step_back + two_step_back      # <- dp[i] = dp[i-1] + dp[i-2]

        #     two_step_back = one_step_back                # Old dp[i-1] becomes next iteration's dp[i-2]

        #     one_step_back = current                      # Current dp[i] becomes next iter's dp[i-1]
        
        # return one_step_back
        

# @lc code=end


# 1. Define f(i) = number of ways to reach position i.

# 1. To reach stair i, it must come from i-1 or i-2.

# 2. Therefore:

#    ways(i) = ways(i-1) + ways(i-2)

# 3. A recursive tree shows overlapping subproblems.

# 4. Use memoization to avoid recomputing.

# 5. Convert memoized recursion into bottom-up DP.

# 6. Observe only the previous two states are needed,
#    so optimize space to O(1).