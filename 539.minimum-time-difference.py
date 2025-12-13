#
# @lc app=leetcode id=539 lang=python3
#
# [539] Minimum Time Difference
#

# @lc code=start
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        timePoints.sort()
        
        def time_to_min(t): 

            hour, min = map(int, t.split(":"))

            return 60 * hour + min
        
        # Take care of wrap-around (last-first) pair  
        res = 24 * 60 - time_to_min(timePoints[-1]) + time_to_min(timePoints[0])

        # Handle adjacent pairs
        for i in range(len(timePoints) - 1): 

            current = time_to_min(timePoints[i + 1])

            prev = time_to_min(timePoints[i])

            diff = current - prev

            res = min(diff, res)
        
        return res


# Handle wrap-around pair across midnight:
# For 2 time points [A, B], compares B -> A (next day)
# For 2+ time points [A, B, C, D, ...], compares last -> first (next day)


# @lc code=end

