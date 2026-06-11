#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # method 1: recursive binary search: O(log n) time; O(log n) space 

        # method 2: iterative binary search: O(log n) time; O(1) space

        l, r = 0, len(nums) - 1

        while l <= r: # Inclusive range [l, r]; Must check when l == r (last element)

            m = l + ((r - l) // 2) # Avoid overflow, compared to m = (l + r) // 2

            if nums[m] == target: 

                return m
            
            elif nums[m] < target: # Too small, search right, i.e., [m + 1, r] 

                l = m + 1
            
            else:                  # Too big, search left, i.e., [l, m - 1]

                r = m - 1
        
        return -1
    

        # TODO
        # method 3 upper bound: O(log n) time; O(1) space 
        # method 4 lower bound: O(log n) time; O(1) space
    

# @lc code=end


# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1


# method 2

# 1. Define the Search Space

# answer in [0, len(nums) - 1] 

# 2. Reframe as a Yes/No Question

# nums[m] == target  → found it, return m immediately
# nums[m] < target   → answer is to the right  → l = m + 1
# nums[m] > target   → answer is to the left   → r = m - 1

# 3. Choose the exit condition 

# Why <=? With a closed interval [l, r], the space is empty when l > r. 

# 4. Return the correct value 

# return m if possible
# return -1 if not possible
