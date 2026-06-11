#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # method 1 binary search I: O(log n) time; O(1) space  

        left = self.binarySearch(nums, target, True)      # O(log n)

        right = self.binarySearch(nums, target, False)    # O(log n)

        return [left, right]

    def binarySearch(self, nums, target, left_most): # left_most == True, look for left most index. Else, look for right most index

        l, r = 0, len(nums) - 1

        i = -1

        while l <= r:

            m = (l + r) // 2

            if nums[m] < target:

                l = m + 1

            elif nums[m] > target:

                r = m - 1

            else:

                i = m

                # Without if else this is just standard binary search 

                if left_most: # Find the leftmost index by searching to the left

                    r = m - 1

                else:         # Find the rightmost index by searching to the right

                    l = m + 1

        return i

               
        # method 2 binary search II: O(log n) time; O(1) space  

        
# @lc code=end


# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# method 1

# 1. Define the Search Space

# answer in [0, len(nums) - 1] 

# 2. Reframe as a Yes/No Question

# Run binary search twice with different behavior on a match:

# #1 pass: find leftmost  → on match, keep searching left  → r = m - 1
# #2 pass: find rightmost → on match, keep searching right → l = m + 1

# On a match, instead of returning immediately like LC 704, you record the candidate and keep narrowing:

# if nums[m] == target:
#     i = m              # record best answer so far
#     if left_most:
#         r = m - 1      # maybe something equal is further left
#     else:
#         l = m + 1      # maybe something equal is further right

# 3. Choose the exit condition 

# Why <=? With a closed interval [l, r], the space is empty when l > r. 

# 4. Return the correct value 

# return i where i holds the last recorded match