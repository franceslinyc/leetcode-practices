#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # # method 1: Prefix & Suffix; O(n) time; O(n) space

        # n = len(nums)

        # res = [0] * n

        # prefix, postfix = [0] * n, [0] * n

        # prefix[0], postfix[n - 1] = 1, 1

        # for i in range(1, n):

        #     prefix[i] = prefix[i - 1] * nums[i - 1]

        # for i in range(n - 2, -1, -1):    # Backward; Build from right 

        #     postfix[i] = postfix[i + 1] * nums[i + 1] 

        # for i in range(n):

        #     res[i] = prefix[i] * postfix[i]

        # return res


        # method 2: Prefix & Suffix (Optimal); O(n) time; O(1) extra space, O(n) space for output array
        
        res = [1] * len(nums)

        prefix = 1

        for i in range(len(nums)): 

            res[i] = prefix 

            prefix *= nums[i]     # Update prefix to include current element for next iteration 

        postfix = 1

        for i in range(len(nums) - 1, -1, -1): 

            res[i] *= postfix
            
            postfix *= nums[i]    # Update postfix to include current element for next iteration 

        return res

# @lc code=end

