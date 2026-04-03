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

        dp[1], dp[2] = 1, 2          # base cases

        for i in range(3, n + 1):    # Start at 3 because we already know dp[1], dp[2]

            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


        # # method 4 dp (space optimized): O(n) time; O(1) space

        # if n <= 2: 

        #     return n

        # one_back = 2

        # two_back = 1

        # for i in range(3, n + 1): 

        #     current = one_back + two_back

        #     two_back = one_back

        #     one_back = current
        
        # return one_back
        

# @lc code=end

