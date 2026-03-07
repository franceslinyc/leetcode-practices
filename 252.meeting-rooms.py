#
# @lc app=leetcode id=252 lang=python3
#
# [252] Meeting Rooms
#

# @lc code=start
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        # method 1: brute force; O(n2) time; O(n) space

        # method 2: sorting; O(nlogn) time; O(n) or O(1) space
        
        intervals.sort() # intervals.sort(key=lambda i: i[0]) works too

        for i in range(1, len(intervals)): 

            interval1 = intervals[i - 1]

            interval2 = intervals[i]

            if interval1[1] > interval2[0]: 

                return False
            
        return True


# @lc code=end

