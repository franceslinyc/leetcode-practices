#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # mehtod 1: two pointers; time O(n), space O(1)

        l, r = 0, len(numbers) - 1

        while l < r: 

            sum_current = numbers[l] + numbers[r]

            if sum_current == target: 

                return [l + 1, r + 1] # Not return [l, r], read the question again!
            
            elif sum_current > target: 

                r -= 1
            
            else: 

                l += 1


        # method 2: binary search; time O(nlogn) space O(1)


# @lc code=end

