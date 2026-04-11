#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # method binary search (one pass): O(log n) time; O(1) space 

        l, r = 0, len(nums) - 1

        while l <= r: 

            m = l + (r - l) // 2

            if nums[m] == target: 

                return m

            # ASK “Which side is sorted, and does the target live there?”

            if nums[l] <= nums[m]: # If left portion is sorted, e.g., [4, 5, 6, 7, 0, 1, 2] because [4, 5, 6, 7] is sorted. 

                if nums[l] <= target <= nums[m]: 

                    r = m - 1      # Search left
                
                else:              # target > nums[m] or target < nums[l]

                    l = m + 1

            else:                  # If right portion sorted, e.g., [5, 6, 7, 0, 1, 2, 4] because [0, 1, 2, 4] is sorted.

                if nums[m] <= target <= nums[r]:

                    l = m + 1      # Search right

                else: 

                    r = m - 1 

        return -1


# We can use a modified binary search by checking which half is sorted at each step and 
# narrowing the search space based on whether the target lies within that sorted portion. 
# This runs in O(log n) time since we halve the search space each iteration, and O(1) space 
# as we only use pointers.


# Idea: 

# Example #1

# nums = [4,5,6,7,0,1,2], target = 0 
#         l           r
# l = 0, r = 6, m = 3 -> nums[3] = 7 -> left [4, 5, 6, 7] is sorted -> Is 4 <= 0 <= 7? No. -> l = m + 1 = 4

# nums = [4,5,6,7,0,1,2]
#                 l   r
# l = 4, r = 6, m = 5 -> nums[5] = 1 -> left [0, 1] is sorted -> Is 0 <=0<=1? Yes. -> r = m - 1 = 4

# nums = [4,5,6,7,0,1,2]
#                 l
#                 r
# l = 4, r = 4, m = 4 -> nums[4] == 0. Find it!

# Example #2

# nums = [0,1,2,4,5,6,7], target = 6
#         l           r
# l = 0, r = 6, m = 3 -> nums[3] = 4 -> left [0,1,2,4] is sorted 

# Example #3
# nums = [6,7,0,1,2,4,5] 
#         l           r
# l = 0, r = 6, m = 3 -> nums[3] = 1 -> right [1,2,4,5] is sorted

# @lc code=end

