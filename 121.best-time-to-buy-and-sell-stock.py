#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # method 1 two pointers: O(n) time; O(1) space
        
        # Similar to LC 122; Look for single largest upward move

        max_profit = 0

        l, r = 0, 1

        for r in range(len(prices)):  # Or while r < len(prices): 

            if prices[r] > prices[l]: # This version ensures no negative profit is calculated 

                profit = prices[r] - prices[l]

                max_profit = max(max_profit, profit)

            else: 

                l = r

            #r += 1 # Always move r 

        return max_profit


        # # method 2 DP: O(n) time; O(1) space

        # max_profit = 0 

        # min_buy = prices[0]

        # for price in prices: 

        #     max_profit = max(max_profit, price - min_buy)

        #     min_buy = min(min_buy, price)

        # return max_profit


# [7, 1, 5, 3, 6, 4]
#  l  r
#     l  r 
#     l     r
#     l        r        <- max profit
#     l           r


# @lc code=end

