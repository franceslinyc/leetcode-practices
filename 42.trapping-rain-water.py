#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:

        # method 1 prefix and suffix arrays
        n = len(height)

        if n == 0: 

            return 0 
        
        left_max = [0] * n

        right_max = [0] * n
        
        left_max[0] = height[0]          # First is 0

        for i in range(1, n):            # Start at 1; Stop at n - 1

            left_max[i] = max(left_max[i - 1], height[i])

        right_max[n - 1] = height[n - 1] # First is n - 1

        for i in range(n - 2, -1, -1):   # Start at n - 2; Stop at 0

            right_max[i] = max(right_max[i + 1], height[i])

        res = 0 

        for i in range(n): 

            res += min(left_max[i], right_max[i]) - height[i]

        return res


        # method 2 two pointers


# height = [0,1,0,2,1,0,1,3,2,1,2,1]
# left_max[0] = 0
# left_max[1] = max(0, 1) = 1
# left_max[2] = max(1, 0) = 1
# left_max[3] = max(1, 2) = 2

# @lc code=end

