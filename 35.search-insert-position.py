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

            if nums[m] >= target:  # m might be the answer, but maybe there’s an earlier one

                r = m              # Keep m in the search space. Else, r = m - 1 will discard m

            elif nums[m] < target: 

                l = m + 1

        return l


# method 2

# [2] target = 1
#  l
#  r 
#  m = (0 + 0) // 2 = 0, value too big, e.g., 2 > 1, search left, i.e., [l, m - 1]
#  l = 0    
#  r = -1
# since 0 > -1: exit 

# [2] target = 3
#  l
#  r
#  m = (0 + 0) // 2 = 0, value too small, e.g., 2 < 3, search right, i.e., [m + 1, r]
#  l = 1
#  r = 0
# since 1 > 0: exit
        

# @lc code=end

