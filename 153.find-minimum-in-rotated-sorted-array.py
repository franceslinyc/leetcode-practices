#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:

        # # method 1 binary search: O(log n) time; O(1) space 
        
        # l, r = 0, len(nums) - 1

        # res = nums[0]

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

            # ASK "Which half is m in: right (clean) or left (rotated)?"
            
            if nums[m] < nums[r]:       # m is in the right (clean) half
                                        # minimum is at m or to the left of m
                r = m                   # keep m in the search space

            else: # nums[m] >= nums[r]  # m is in the left (rotated) half
                                        # minimum is to the right of m
                l = m + 1               # m is definitely not the minimum

        return nums[l]


# @lc code=end


# We can use binary search to compare the middle element with the right boundary to determine 
# which half contains the minimum, always keeping the candidate in the search space until it 
# converges to a single index. This runs in O(log n) time since we halve the search space each
# step, and O(1) space as we only use pointers.


# 1. Define the Search Space

# answer in [0, len(nums) - 1] 

# 2. Reframe as a Yes/No Question

# A rotated array has two halves. The right half is clean (fully sorted). The left half is rotated (starts high).
# "Is m in the right (clean) half or left (rotated) half?"

# nums[m] < nums[r]  → m is in right half → minimum is at m or left of m → r = m
# nums[m] >= nums[r] → m is in left half  → minimum is right of m        → l = m + 1
# (nums[m] never == nums[r])

# 3. Choose the exit condition 

# Why <? With a half-open interval [l, r), the space is empty when l == r. 

# 4. Return the correct value 

# At exit, l == r. The search space has collapsed to one index, which is the minimum.


# Idea: 
#             m              
# nums = [1,2,3,4,5] output = 1
# nums[2] = 3 < 5 -> Search left

#             m         
# nums = [3,4,5,1,2] output = 1
# nums[2] = 5 >= 2 -> Search right

