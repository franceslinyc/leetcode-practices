#
# @lc app=leetcode id=253 lang=python3
#
# [253] Meeting Rooms II
#

# @lc code=start
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        # method 1: Priority Queues; Min Heap; O(nlogn) time; O(n) space

        # method 2: Chronological Ordering; Two Pointers; O(nlogn) time; O(n) space

        start_time = sorted(i[0] for i in intervals) # O(nlogn) worst case

        end_time = sorted(i[1] for i in intervals)

        res, count = 0, 0 

        s, e = 0, 0 # s: start pointer; e: end pointer 

        while s < len(start_time):    # Should be len(start_time), not len(intervals)

            if start_time[s] < end_time[e]: 

                count += 1

                s += 1

            else: 

                count -= 1

                e += 1

            res = max(res, count)

        return res


# Details: 
#
# e.g., intervals = [[0,30],[5,10],[15,20]]
# start time = [0, 5, 15]
# end time = [10, 20, 30]
#
#
# s=0 e=0
# 0 < 10 -> start meeting (increment count)
# s+=1 (next start time)

# s=1 e=0
# 5 < 10 -> start meeting (increment count)
# s+=1 (next start time)

# s=2 e=0
# 15 >= 10 -> meeting ended (decrement count)
# e+=1 (next end time)


# @lc code=end

