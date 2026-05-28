#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:

        # # method 1 brute-force: O(2^n) time; O(n) space

        # if n <= 1: 

        #     return n

        # return self.fib(n - 1) + self.fib(n - 2) # O(n) space for recursion call


        # # method 2 dp top-down (memoization): O(n) time; O(n) space

        # memo = {0:0, 1:1}

        # def f(n): 

        #     if n in memo: 

        #         return memo[n]

        #     memo[n] = f(n - 1) + f(n - 2)

        #     return memo[n]

        # return f(n)


        # memo = {} # Remove base cases

        # def f(n): 

        #     if n <= 1:     # Base case 

        #         return n

        #     if n in memo:  # If Subproblem in memo map

        #         return memo[n]

        #     memo[n] = f(n - 1) + f(n - 2)

        #     return memo[n]

        # return f(n)  


        # method 3 dp bottom-up: O(n) time; O(n) space

        if n <= 1: 

            return n

        dp = [0] * (n + 1)           # dp[i] = the ith Fibonacci number; n + 1 because we need to go to go from 0 to n inclusive.
        
        dp[0], dp[1] = 0, 1          # base cases
 
        for i in range(2, n + 1):    # Start at 2 because we already know dp[0], dp[1]

            dp[i] = dp[i - 1] + dp[i - 2]
 
        return dp[n] 


# @lc code=end


# F(0) = 0                     <- base cases
# F(1) = 1                     <- base cases
# F(2) = F(1) + F(0)
# F(3) = F(2) + F(1) 
# F(n) = F(n - 1) + F(n - 2)   <- formula 


# method 1: O(2^n) time and O(n) space. 
# 
#              f(6)
#           /        \
#       f(4)          f(5)
#      /    \        /     \
#  f(2)    f(3)  f(3)     f(4)
#           / \    / \     /   \
#        f(1) f(2)f(1)f(2)f(2) f(3)
#                             / \
#                          f(1) f(2)