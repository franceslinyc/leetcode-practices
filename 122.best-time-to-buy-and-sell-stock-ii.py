#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Greedy 

        # Look for all upward moves; Similar to LC 121 but key is any big upward move can be broken into consecutive smaller upward moves

        profit = 0

        for i in range(1, len(prices)):

            if prices[i] - prices[i - 1] > 0: 

                profit += (prices[i] - prices[i - 1]) # Increment profit; Can sell and buy multiple times 

        return profit 
    
        # DP, Top-Down

        # DP, Bottom-Up


# @lc code=end

