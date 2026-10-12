#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:

            # method 1: two pointers; time O(n^3), where n is length of the given array; space O(1) + O(n) for sort() excluding output list. 

            nums.sort()

            res = []

            for i in range(len(nums)): # for i, a in enumerate(nums): 

                #   if a > 0: # Unlike LC 15, not summing up to 0 this time, sum to a target.

                #         break

                if i > 0 and nums[i] == nums[i-1]:          # Becasue i starts at 0

                     continue

                for j in range(i+1, len(nums)): 

                     if j > i + 1 and nums[j] == nums[j-1]: # Because j starts at j + 1

                          continue 

                     l, r = j + 1, len(nums) - 1

                     while l < r: 
                          

                          current_sum = nums[i] + nums[j] + nums[l] + nums[r]

                          if current_sum == target: 
                            
                            res.append([nums[i], nums[j], nums[l], nums[r]])

                            l += 1

                            while l < r and nums[l] == nums[l-1]: 

                                l += 1

                          elif current_sum < target: 

                               l += 1

                          else: 

                               r -= 1

            return res
                
                                
# @lc code=end

