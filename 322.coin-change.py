#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # # method 2 dp (top-down): O(N * T) time; O(T) space, where N is the length of the array and T is the given amount. 

        # memo = {}  # memo map stores key:value = amount: min number of coins to make that amount

        # def f(amount):

        #     if amount == 0:

        #         return 0

        #     if amount in memo:

        #         return memo[amount]

        #     res = 1e9

        #     for coin in coins:

        #         if amount - coin >= 0:

        #             res = min(res, 1 + f(amount - coin))

        #     memo[amount] = res

        #     return res

        # res = f(amount)

        # return -1 if res >= 1e9 else res


        # method 3 dp (bottom-up): O(N * T) time; O(T) space, where N is the length of the array and T is the given amount. 

        dp = [float('inf')] * (amount + 1)

        dp[0] = 0              # base case
                               # dp[i] store min number of coins to make amount i

        for a in range(1, amount + 1):

            for coin in coins:

                if a - coin >= 0: 

                    dp[a] = min(dp[a], 1 + dp[a - coin])

                                # dp[a]: best so far for amount a
                                # 1: current coin; dp[a - coin]: min number of coins for remainder

        return dp[amount] if dp[amount] != float('inf') else -1
        
        
# @lc code=end


# e.g., coins = [1,2,5], amount = 11, output = 3

# dp[i] = min number of coins needed to make amount i

# dp[0] = 0
# dp[1] = 1
# dp[2] = min(2, 1) = 1

# use coin 1 -> 1 (current coin) + dp[2-1] (min number of coins for remainder) = 1 + dp[1] = 1 + 1 = 2
# use coin 2 -> 1 + dp[2-2] = 1 + dp[0] = 0 + 1 = 1
# use coin 5 -> 2-5 = -3 < 0, skip

# dp[3] = min(2, 2) = 2

# use coin 1 -> 1 + dp[3-1] = 1 + dp[2] = 2
# use coin 2 -> 1 + dp[3-2] = 1 + dp[1] = 2
# use coin 5 -> 3-5 = -2 < 0, skip

