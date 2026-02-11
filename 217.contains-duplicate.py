#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        this_set = set()
        for num in nums: 
            if num in this_set: 
                return True
            this_set.add(num)
        return False

        
# @lc code=end

