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

        q = deque()  # Store indices (not values) in decreasing order of values, so q[0] (front of deque) contains 
                     # the index of the maximum value, AKA monotonically decreasing queue
                     # Store indices or else we can't compare positiom in step 2
                     # Store a running history of indices across all past r values 

        l = 0

        for r in range(len(nums)): 

            # Maintain the monotonically decreasing queue

            while q and nums[q[-1]] < nums[r]:

                q.pop()

            q.append(r)

            # Remove indice from the front that are outside the window 

            while q and l > q[0]: # Careful! q holds indices from past iterations

                q.popleft()

            # When the widown is full, record the max and move l forward

            #if (r + 1) >= k:      # Careful! r + 1 = elements seen so far; l only moves here (l does not move regularly)

            if (r - l + 1) >= k: 

                output.append(nums[q[0]]) # Leftmost position is always the max value  

                l += 1

        return output        


# @lc code=end


# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]

# l=0
# [1, 3, -1, -3, 5, 3, 6, 7]
#  r=0
 
#   Step 1: q empty → append 0        q: [0]      values: [1]
#   Step 2: q[0]=0, l=0 → inside
#   Step 3: r+1=1 < 3 → skip

# ─────────────────────────────────────
# l=0
# [1, 3, -1, -3, 5, 3, 6, 7]
#     r=1

#   Step 1: nums[0]=1 < 3 → pop 0
#           append 1                   q: [1]      values: [3]
#   Step 2: q[0]=1, l=0 → inside
#   Step 3: r+1=2 < 3 → skip

# ─────────────────────────────────────
# l=0
# [1, 3, -1, -3, 5, 3, 6, 7]
#         r

#   Step 1: nums[1]=3 > -1 → keep
#           append 2                   q: [1,2]    values: [3,-1]
#   Step 2: q[0]=1, l=0 → inside
#   Step 3: r+1=3 >= 3 ✓ → output=[3], l moves to 1

# ─────────────────────────────────────
#     l=1
# [1, 3, -1, -3, 5, 3, 6, 7]
#             r

#   Step 1: nums[2]=-1 > -3 → keep
#           append 3                   q: [1,2,3]  values: [3,-1,-3]
#   Step 2: q[0]=1, l=1 → inside (1 >= 1)
#   Step 3: r+1=4 >= 3 ✓ → output=[3,3], l moves to 2

# ─────────────────────────────────────
#     l=2
# [1, 3, -1, -3, 5, 3, 6, 7]
#                   r

#   Step 1: nums[3]=-3 < 5 → pop 3
#           nums[2]=-1 < 5 → pop 2
#           nums[1]=3  < 5 → pop 1
#           append 4                   q: [4]      values: [5]
#   Step 2: q[0]=4, l=2 → inside
#   Step 3: r+1=5 >= 3 ✓ → output=[3,3,5], l moves to 3
