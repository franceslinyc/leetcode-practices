#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]): # Constructor; Set up the object

        self.prefix = []                 # Initialize attribute or propertie 

        current = 0 

        for num in nums: 

            current += num 

            self.prefix.append(current)
        
    def sumRange(self, left: int, right: int) -> int: # Method 

        # (0 -> right) - (0 -> left-1) = (left -> right)
        
        right_sum = self.prefix[right]

        left_sum = self.prefix[left - 1] if left > 0 else 0 

        return right_sum - left_sum
        
        
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end

