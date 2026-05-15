#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # method 1: min heap: O(N + K log N) time; O(N) space

        min_heap = [] # O(N) space

        for point in points: # for x, y in points:# O(N) time  

            x = point[0]

            y = point[1]

            distance = sqrt((x-0)**2 + (y-0)**2)  # Don't necessarily need sqr 

            min_heap.append([distance, x, y])

        heapify(min_heap)  # O(N) time

        res = []      # O(K) space

        for _ in range(k): # O(K) time

            distance, x, y = heappop(min_heap)   # O(log N) time

            res.append([x, y])

        return res


        # method 2: quick select: O(N), O(N^2) time worst case; O(1) space
      
        
# @lc code=end

