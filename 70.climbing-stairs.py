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

        dp = [0] * (n + 1)           # dp[i] = number of ways to reach step i

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


# n = 1 -> F(1) = 1 way               <- base cases
# n = 2 -> F(2) = 2 way               <- base cases
# n = 3 -> F(3) = F(2) + F(1) = 3 way
# n = 4 -> F(4) = F(3) + F(2) = 5 way
#          F(n) = F(n - 1) + F(n - 2) <- formula 

# F(3) = 3 way
# {1+1+1, 1+2, 2+1} 

# F(4) = 5 way
# {1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2} 