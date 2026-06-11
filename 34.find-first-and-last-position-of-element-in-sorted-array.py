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


        # method 1 variation via Coding Interview Patterns: O(log n) time; O(1) space  
        
        # method 2 binary search II: O(log n) time; O(1) space  

        
# @lc code=end

