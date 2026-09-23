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

            # ASK "Which side of m is sorted? Does target live there?"

            if nums[m] < nums[r]: 

                if nums[m] <= target <= nums[r]: 

                    l = m + 1
                
                else: 

                    r = m - 1
            
            else: # nums[m] >= nums[r]                  

                if nums[l] <= target <= nums[m]:

                    r = m - 1

                else: 

                    l = m + 1

        return -1


# @lc code=end


# We can use a modified binary search by checking which half is sorted at each step and 
# narrowing the search space based on whether the target lies within that sorted portion. 
# This runs in O(log n) time since we halve the search space each iteration, and O(1) space 
# as we only use pointers.


# 1. Define the Search Space

# answer in [0, len(nums) - 1]

# 2. Reframe as a Yes/No Question

# A rotated array has two halves. The right half is clean (fully sorted). The left half is rotated (starts high).
# "Is m in the right (clean) half or left (rotated) half? Does target live there?"

# Return m immediately if nums[m] == target
# nums[m] <  nums[r] → right half sorted → if nums[m] <= target <= nums[r]: l = m + 1, else r = m - 1
# nums[m] >= nums[r] → left half sorted  → if nums[l] <= target <= nums[m]: r = m - 1, else l = m + 1

# 3. Choose the exit condition

# Why <=? With a closed interval [l, r], the space is empty when l > r.

# 4. Return the correct value

# Return -1 if target never found.
