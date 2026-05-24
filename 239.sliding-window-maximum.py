#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # method 1: heap

        # method 2: dp

        # method 3: deque: O(n) time; O(n) space

        output = []

        q = deque()  # Store indices in decreasing order of values, so q[0] (front of deque) contains 
                     # the index of the maximum value, AKA monotonically decreasing queue
                     # Store indeices or else we can't compare positio in step 2

        l = 0

        for r in range(len(nums)): 

            # Maintain the monotonically decreasing queue

            while q and nums[q[-1]] < nums[r]:

                q.pop()

            q.append(r)

            # Remove indices from the front that are outside the window 

            while q and l > q[0]:

                q.popleft()

            # When the widown is full, record the max and move l forward

            if (r + 1) >= k:

                output.append(nums[q[0]]) # Leftmost position is always the max value  

                l += 1

        return output        


# @lc code=end

