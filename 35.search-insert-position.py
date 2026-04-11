#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        # # method 2: binary search II: O(log n) time; O(1) space  

        # l, r = 0, len(nums) - 1

        # while l <= r: 

        #     m = (l + r) // 2

        #     if nums[m] == target: 

        #         return m

        #     elif nums[m] < target: # value too small, search right, i.e., [m + 1, r]

        #         l = m + 1
            
        #     else:                  # value too big, search left, i.e., [l, m - 1]

        #         r = m - 1

        # return l 

        # method 3: binary search (lower bound): O(log n) time; O(1) space  

        l, r = 0, len(nums)  # Search in [l, r); Allow insert at the end of the array

        while l < r:         # Stop at l == r 

            m = (r + l) // 2

            # THINK "Find first index where value >= target" 

            if nums[m] >= target:  # m might be the answer, but maybe there’s an earlier one

                r = m              # Keep m in the search space. Else, r = m - 1 will discard m

            elif nums[m] < target: 

                l = m + 1          # m is definitely too small

        return l # Return the first position where nums[m] >= target or the correct insertion point


# method 3

# Ideas: 

# nums = [1, 3, 3, 5, 7], target = 3

# range = [0, 5)

# m = (0 + 5) // 2 = 2, since nums[2] = 3 == 3, search left, i.e., 
# range = [0, 2)

# m = (0 + 2) // 2 = 1, since nums[1] = 3 == 3, search left, i.e., 
# range = [0, 1)

# m = (0 + 1) // 2 = 0, since nums[0] = 1 < 3, search right, i.e., 
# range = [1, 1) 
# Exit while loop since l == r and return l = 1        


# @lc code=end

