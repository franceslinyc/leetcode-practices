#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
class MedianFinder:

    def __init__(self):

        self.left = []  # max_heap

        self.right = [] # min_heap
        
    def addNum(self, num: int) -> None:

        if self.right and num > self.right[0]: 

            heappush(self.right, num) # Not self.right.append(num); this gives list only not heap

        else: 

            heappush(self.left, -1 * num)

        # Rebalance

        if len(self.left) > len(self.right) + 1: 

            val = -1 * heappop(self.left)

            heappush(self.right, val)

        if len(self.left) + 1 < len(self.right): 

            val = heappop(self.right)

            heappush(self.left, -1 * val)
        

    def findMedian(self) -> float:

        if len(self.left) > len(self.right): 

            return -1 * self.left[0]

        elif len(self.left) < len(self.right): 

            return self.right[0]

        else: # even number case

            return (-1 * self.left[0] + self.right[0]) / 2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

