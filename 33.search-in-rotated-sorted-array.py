#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # method 1 binary search (one pass): O(log n) time; O(1) space 

        l, r = 0, len(nums) - 1

        while l <= r: 

            m = l + (r - l) // 2

            if nums[m] == target: 

                return m

            # ASK “Which half is sorted? Does target live there?”

            #                                            m
            # If left portion [l:m] is sorted, e.g., [4, 5, 6, 7, 0, 1, 2] because [4, 5, 6, 7] is sorted. 
            # If the target falls in this range, search the left subarrary. Else, go to the right side.

            if nums[l] <= nums[m]: 

                if nums[l] <= target <= nums[m]: 

                    r = m - 1
                
                else:              # target > nums[m] or target < nums[l]

                    l = m + 1      # Else, go right
            
            #                                          m
            # If right portion [m:r] sorted, e.g., [5, 6, 7, 0, 1, 2, 4] because [0, 1, 2, 4] is sorted.
            # If the target falls in this range, search the right subarrary. Else, go to the left side.

            else: # nums[l] > nums[m]                  

                if nums[m] <= target <= nums[r]:

                    l = m + 1 

                else: 

                    r = m - 1      # Else, go left 

        return -1


# @lc code=end


# We can use a modified binary search by checking which half is sorted at each step and 
# narrowing the search space based on whether the target lies within that sorted portion. 
# This runs in O(log n) time since we halve the search space each iteration, and O(1) space 
# as we only use pointers.


# 1. Define the Search Space

# answer in [0, len(nums) - 1]

# 2. Reframe as a Yes/No Question

# A rotated array has two halves. At any midpoint, one half is always sorted.
# "Is the left half sorted? Does target live there?"

# nums[l] <= nums[m] → left half sorted  → if nums[l] <= target <= nums[m]: r = m - 1, else l = m + 1
# nums[l] >  nums[m] → right half sorted → if nums[m] <= target <= nums[r]: l = m + 1, else r = m - 1
# Return m immediately if nums[m] == target

# 3. Choose the exit condition

# Why <=? With a closed interval [l, r], the space is empty when l > r.

# 4. Return the correct value

# Return -1 if target never found.


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