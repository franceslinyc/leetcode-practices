#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#

# @lc code=start
class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.k = k

        self.min_heap = nums

        heapify(self.min_heap)           # Rearranges list into a valid min heap (default)

        while len(self.min_heap) > k:          

            heappop(self.min_heap)       # Remove smallest element to keep only k largest; heappop ALWAYS remove smallest element 

    def add(self, val: int) -> int:

        # Careful! Remember to use self. to access instance varaible
        
        heappush(self.min_heap, val)     # Maintain heap property after insertion; heappush Insert into heap while maintaining order 

        if len(self.min_heap) > self.k: 

            heappop(self.min_heap)

        return self.min_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end


# import heapq
# heapq.heapify
# heapq.heappush Insert into heap while maintaining order 
# heapq.heappop  ALWAYS remove smalles element 


# e.g., 
# ["KthLargest", "add", "add", "add", "add", "add"]
# [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

# [4, 5, 8, 2]
# [2, 4, 5, 8]
# keep [4, 5, 8]
# 3rd largest = 4

# add 3
# [4, 5, 8, 2, 3]
# [2, 3, 4, 5, 8]
# keep [4, 5, 8]
# 3rd largest = 4

# add 5
# [4, 5, 8, 2, 3, 5]
# [2, 3, 4, 5, 5, 8]
# keep [5, 5, 8]
# 3rd largetst = 5

# add 10
# [4, 5, 8, 2, 3, 5, 10]
# [2, 3, 4, 5, 5, 8, 10]
# keep [5, 8, 10]
# 3rd largetst = 5