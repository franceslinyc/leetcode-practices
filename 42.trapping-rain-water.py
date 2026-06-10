#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:

        # # method 1 prefix and suffix arrays: O(n) time; O(n) space

        # n = len(height)

        # if n == 0: 

        #     return 0 
        
        # left_max = [0] * n

        # right_max = [0] * n
        
        # left_max[0] = height[0]          # First is 0

        # for i in range(1, n):            # Start at 1; Stop at n - 1

        #     left_max[i] = max(left_max[i - 1], height[i])

        # right_max[n - 1] = height[n - 1] # First is n - 1

        # for i in range(n - 2, -1, -1):   # Start at n - 2; Stop at 0

        #     right_max[i] = max(right_max[i + 1], height[i])

        # res = 0 

        # for i in range(n): 

        #     res += min(left_max[i], right_max[i]) - height[i]

        # return res


        # method 2 two pointers: O(n) time; O(1) space

        res = 0

        l, r = 0, len(height) - 1

        left_max, right_max = height[l], height[r]

        while l < r: 

            if left_max <= right_max:               # Left is the bottleneck wall because water only fill out to the shorter wall

                l += 1                              # Move l up

                left_max = max(left_max, height[l]) # Maintain the tallest left wall seen so far

                res += 1 * (left_max - height[l]) 

                # water per cell = base * (bottleneck wall - current height)
                # = 1 * (min(left_max, right_max) - height[l])
                # since left_max <= right_max, min(left_max, right_max) = left_max
                # = 1 * (left_max - height[l])

            else: 

                r -= 1

                right_max = max(right_max, height[r])

                res += 1 * (right_max - height[r])

        return res


# @lc code=end


# Water at each position depends on the min of the max height to its left and right, 
# i.e., water = base × height = 1 × (min(left_max, right_max) - height[i]).
# The shorter height between left_max and right_max determines the water level, so 
# we can safely ignore the taller height, e.g., if left_max < right_max, then water
# is determined only by left_max.


# e.g., 
# height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6

#  l                     r
# [0,1,0,2,1,0,1,3,2,1,2,1]
# left_max=0, right_max=1, 0 <= 1 → move l (l at 1 now)
# left_max = max(0, height[1]) = max(0,1) = 1, water = 1 * (1-1) = 0

#    l                   r
# [0,1,0,2,1,0,1,3,2,1,2,1]
# left_max=1, right_max=1, 1 <= 1 → move l (l at 2 now)
# left_max = max(1, height[2]) = max(1,0) = 1, water = 1 * (1-0) = 1 ✓

#      l                 r
# [0,1,0,2,1,0,1,3,2,1,2,1]
# left_max=1, right_max=1, 1 <= 1 → move l (l at 3 now)
# left_max = max(1, height[3]) = max(1,2) = 2, water = 1 * (2-2) = 0
