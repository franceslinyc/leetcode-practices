#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # # method 1 brute force
        # nums.sort()

        # method 2 three pointers - I (optimized quick sort): O(n) time; O(1) space
        
        l, r = 0, len(nums) - 1

        i = 0

        def swap(i, j):

            temp = nums[i]

            nums[i] = nums[j]

            nums[j] = temp

        while i <= r:

            if nums[i] == 0:   # Move 0 to the left side

                swap(l, i)

                l += 1

            elif nums[i] == 2: # Move 2 to the right side

                swap(i, r)

                r -= 1

                i -= 1         # Do not increment i since the swapped element needs to be checked 
                               # Swapping with the right brings in unknown data

            # Increment i for values that are already correctly placed, i.e., 0, 1
            # 0 is already moved to correct position
            # Leave 1 it in the middle region and just move forward
            i += 1        
        

# @lc code=end

