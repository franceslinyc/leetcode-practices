#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # method 1 sorting 
        intervals.sort(key=lambda pair: pair[0]) # Sort intervals based on start value
        output = [intervals[0]]

        for start, end in intervals[1:]: # Get start, end value of CURRENT interval

            last_end = output[-1][1]     # Get end value of PREVIOUS interval 

            if start <= last_end: 

                output[-1][1] = max(last_end, end)

            else: 

                output.append([start, end])

        return output
    
        # method 2 greedy

        
# @lc code=end

