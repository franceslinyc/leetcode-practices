#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:

        # # method 1 binary search: O(log n) time; O(1) space 

        # res = nums[0]
        
        # l, r = 0, len(nums) - 1

        # while l <= r: 

        #     if nums[l] < nums[r]: 

        #         res = min(res, nums[l])

        #         break

        #     m = l + (r - l) // 2

        #     res = min(res, nums[m])

        #     if nums[m] >= nums[l]: # nums[m] in left side, go right, i.e., [m + 1, r]

        #         l = m + 1

        #     else: 

        #         r = m - 1

        # return res


        # method 2 binary search (lower bound): O(log n) time; O(1) space 

        l, r = 0, len(nums) - 1

        while l < r: 

            m = l + (r - l) // 2

            # ASK “Which side contains the rotation point (the minimum)?”
            
            if nums[m] < nums[r]: # Right side is clean, so pivot must be on the left? 
                                  # Minimum is at m or to the left

                r = m             # Keep m in the search space

            else:                 # Minimum is to the right

                l = m + 1         # m is definitely too small

        return nums[l]


# We can use binary search to compare the middle element with the right boundary to determine 
# which half contains the minimum, always keeping the candidate in the search space until it 
# converges to a single index. This runs in O(log n) time since we halve the search space each
# step, and O(1) space as we only use pointers.

# Idea: 

# nums = [1,2,3,4,5] output = 1
# nums[2] = 3 < 5 -> Search left

# nums = [3,4,5,1,2] output = 1
# nums[2] = 5 >= 2 -> Search right

# @lc code=end

