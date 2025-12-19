#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # method 1 two pointers
        
        max_profit = 0

        l, r = 0, 1

        while r < len(prices): 

            if prices[r] < prices[l]: 

                l = r
            
            profit = prices[r] - prices[l]

            max_profit = max(max_profit, profit)

            r += 1

        return max_profit
    
        # method 2 DP


# @lc code=end

