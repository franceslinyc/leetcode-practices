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

        heapq.heapify(self.min_heap)           # Rearranges list into a valid min heap (default)

        while len(self.min_heap) > k:          

            heapq.heappop(self.min_heap)       # Remove smallest element to keep only k largest

    def add(self, val: int) -> int:

        # Careful! Remember to use self. to access instance varaible
        
        heapq.heappush(self.min_heap, val)     # Maintains heap property after insertion

        if len(self.min_heap) > self.k: 

            heapq.heappop(self.min_heap)

        return self.min_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

