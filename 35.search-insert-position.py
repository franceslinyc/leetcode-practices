#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # method 2: binary search II (standard binary search): O(log n) time; O(1) space  

        l, r = 0, len(nums) - 1

        while l <= r: 

            m = (l + r) // 2

            if nums[m] == target: 

                return m

            elif nums[m] < target: # value too small, search right, i.e., [m + 1, r]

                l = m + 1
            
            else:                  # value too big, search left, i.e., [l, m - 1]

                r = m - 1

        return l 


        # # method 3: binary search (lower bound): O(log n) time; O(1) space  

        # l, r = 0, len(nums)  # Search in [l, r); Allow insert at the end of the array

        # while l < r:         # Stop at l == r 

        #     m = (r + l) // 2

        #     # ASK "Find first index where value >= target" 

        #     if nums[m] >= target:  # m might be the answer, but maybe there’s an earlier one

        #         r = m              # Keep m in the search space. Otherwise, r = m - 1 will discard m

        #     elif nums[m] < target: 

        #         l = m + 1          # m is definitely too small

        # return l # Return the first position where nums[m] >= target or the correct insertion point


# @lc code=end


# Input: nums = [1,3,5,6], target = 5
# Output: 2      F F T T

# Input: nums = [1,3,5,6], target = 2
# Output: 1      F T T T

# Input: nums = [1,3,5,6], target = 7
# Output: 4      F F T T


# method 3

# 1. Define the Search Space

# answer in [0, len(nums)] 

# 2. Reframe as a Yes/No Question

# "Find the first index where some condition flips from False to True"
# "Find the first value greater or equal to target"

# nums[m] >= target

#     r = m     # m could be the answer 

# else 

#     l = m + 1 #

# 3. Choose the exit condition 

# Why not <=? Because r is the exclusive boundary half-open interval [l, r), 
# i.e., the space is empty (nothing else to search aka converge) when l == r. 

# 4. Return the correct value 

# At exit, l == r. They've converged on the first index where nums[i] >= target.