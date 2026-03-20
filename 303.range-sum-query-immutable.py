#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]): # Constructor; Set up the object

        self.prefix = []                 # Initialize attribute or property

        current = 0 

        for num in nums: 

            current += num 

            self.prefix.append(current)
        
    def sumRange(self, left: int, right: int) -> int: # Method 

        right_sum = self.prefix[right]   # Sum up to right

        left_sum = self.prefix[left - 1] if left > 0 else 0 # Sum up to left (or more like left - 1)

        return right_sum - left_sum


# e.g., [-2, 0, 3, -5, 2, -1]
#     ->[-2,-2, 1, -4,-2, -3]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)                  # Call __init__ to create object/instance
# param_1 = obj.sumRange(left,right)    # Call method on object 
# @lc code=end

