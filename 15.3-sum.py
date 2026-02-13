#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # method 1: two pointers; time O(n), space O(1)

        nums.sort()

        res = []

        for i, num in enumerate(nums): 

            if num > 0: # Because the array is sorted, if the first number is 0, the rest cannot sum to 0.

                break

            # Skip duplicate for the first number, i.e., exit the loop. 
            
            if i > 0 and num == nums[i - 1]:  

                continue 

            l, r = i + 1, len(nums) - 1        # Similar to LC 167 Two Sum II

            while l < r: 

                sum_total = num + nums[l] + nums[r]

                if sum_total == 0: 

                    res.append([num, nums[l], nums[r]])
                 
                    l += 1

                    r -= 1

                    # Skip duplicates for left pointer
                    
                    while nums[l] == nums[l - 1] and l < r: # Not if nums[l] == nums[l - 1] and l < r:

                        l += 1

                elif sum_total > 0: 

                    r -= 1

                else: 

                    l += 1
            
        return res # Careful! Need to be outside the for loop.


        # method 2: hash map; time O(n), space O(n)


# @lc code=end

