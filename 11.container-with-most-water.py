#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:

        # method 1: brute force: time O(n^2); space O(1)
    
        # method 2: two pointers: time O(n); space O(1)

        max_area = 0 

        l, r = 0, len(height) - 1 

        while l < r: 

            base = r - l     # ! Careful! Not l - r

            area = base * min(height[l], height[r])

            max_area = max(max_area, area)

            # Move the pointer at the shorter height, because shrinking the width only helps if 
            # we can potentially find a taller height to increase the area.
                
            if height[l] <= height[r]: 

                l += 1   # Move past the shorter height (height[l]) and try to find a taller one

            else: 

                r -= 1
        
        return max_area


# @lc code=end

