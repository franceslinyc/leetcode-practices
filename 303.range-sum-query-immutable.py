#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#

# @lc code=start
class NumArray:

    # def __init__(self, nums: List[int]): # Constructor; Set up the object

    #     self.prefix = []

    #     cur = 0

    #     for num in nums:

    #         cur += num

    #         self.prefix.append(cur)
        
    # def sumRange(self, left: int, right: int) -> int: # Method 

    #     right_sum = self.prefix[right]

    #     left_sum = self.prefix[left - 1] if left > 0 else 0 # Guard against left - 1 = 0 - 1 = - 1 

    #     return right_sum - left_sum

    def __init__(self, nums: List[int]): 

        self.prefix = [nums[0]]

        # for i in range(1, len(nums)): 

        #     self.prefix.append(self.prefix[-1] + nums[i]) # Prev prefix sum + current

        for num in nums: 

            self.prefix.append(self.prefix[-1] + num)
        
    def sumRange(self, left: int, right: int) -> int: 

        if left == 0: 

            return self.prefix[right]

        return self.prefix[right] - self.prefix[left - 1]
    

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)                  # Call __init__ to create object/instance
# param_1 = obj.sumRange(left,right)    # Call method on object 
# @lc code=end


#            l       r
# nums   = [-2,  0,  3, -5,  2, -1]
# prefix = [-2, -2,  1, -4, -2, -3]

# #1 case
#           l = 0    r = 2
# nums   = [-2,  0,  3, -5,  2, -1]
# prefix = [-2, -2,  1, -4, -2, -3]
# res = 1 = prefix[r] = 1

# #2 case
#                    l = 2       r = 5
# nums   = [-2,  0,  3, -5,  2, -1]
# prefix = [-2, -2,  1, -4, -2, -3]
# res = -1 = prefix[r] - prefix[l-1] = (-3) - (-2)
