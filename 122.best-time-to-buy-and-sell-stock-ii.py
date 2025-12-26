#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0

        l, r = 0, 1

        while r < len(prices): 

            if prices[l] < prices[r]: 

                profit = prices[r] - prices[l]

                max_profit += profit

            l += 1
            r += 1

        return max_profit 


# @lc code=end

