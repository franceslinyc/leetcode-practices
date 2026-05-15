#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # method 1: min heap: O(N log K) time; O(K) space

        # Similar to LC 703

        # Careful! Don't use heapify(nums) since this builds heap ds with size n (more work)

        min_heap = []      

        for num in nums:   # O(N) time

            heapq.heappush(min_heap, num)  # O(log K) time (log because heap is a binary heap; O(K) space (heap size is at most K+1)

            if len(min_heap) > k: 

                heapq.heappop(min_heap)    # O(log K) time; O(K) space

        return min_heap[0]   


        # method 2: quick select: O(N), O(N^2) time worst case; O(N) space
        

        # method 3: quick select, optimal: O(N), O(N^2) time worst case; O(1) space
        

# @lc code=end

