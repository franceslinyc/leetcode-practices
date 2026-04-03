#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:

        # # method 1 brute-force: O(2^n) time; O(n) space

        # if n == 0: 

        #     return 0

        # if n == 1: 

        #     return 1

        # return self.fib(n - 1) + self.fib(n - 2) # O(n) space for recursion call


        # # method 2 dp top-down (memoization): O(n) time; O(n) space

        # memo = {0:0, 1:1}

        # def f(x): 

        #     if x in memo: 

        #         return memo[x]

        #     memo[x] = f(x - 1) + f(x - 2)

        #     return memo[x]

        # return f(n)


        # method 3 dp bottom-up: O(n) time; O(n) space

        if n == 0: 

            return 0

        if n == 1: 

            return 1        

        dp = [0] * (n + 1)           # dp[i] = the ith Fibonacci number
        
        dp[0], dp[1] = 0, 1
 
        for i in range(2, n + 1):    # Start at 2 because we already know dp[0], dp[1]

            dp[i] = dp[i - 1] + dp[i - 2]
 
        return dp[n] 


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


# @lc code=end

