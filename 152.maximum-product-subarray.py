#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # res = nums[0]

        # current_max, current_min = 1, 1 # Netural value

        # for num in nums: 

        #     if num == 0: 

        #         current_max, current_min = 1, 1

        #         continue

        #     tmp = current_max * num
            
        #     current_max = max(current_max * num, current_min * num, num)

        #     current_min = min(tmp, current_min * num, num)

        #     res = max(res, current_max)

        # return res


        # method 3 Kadane's Algorithm: O(N) time; O(1) space

        res = nums[0]

        current_min, current_max = 1, 1

        for num in nums: 

            tmp = current_max * num
            
            current_max = max(current_max * num, current_min * num, num)

                            # current_max * num: Extend previous max
                            # current_min * num: Maybe the worst can flip to the best, e.g., negative * negative
                            # num: Restart subarray, e.g., current num is larger than any product chain, zero

            current_min = min(tmp, current_min * num, num) # Track the most negative value ready to flip

            res = max(res, current_max)

        return res


        # method 4 Prefix & Suffix: O(N) time; O(1) space

       
# @lc code=end


# e.g., [2,3,-2,4] output 6

# iter 0
# tmp = 2, current_max = 2, current_min = 2, res = 2
# iter 1
# tmp = 6, current_max = 6, current_min = 3, res = 6
# iter 2
# tmp = -12, current_max = -2, current_min = -12, res = 6
# iter 3
# tmp = -8, current_max = 4, current_min = -48, res = 6


# e.g., [-2,0,-1] output 0

# e.g., [-2,0,-1,1] output 1

# e.g., [-2,0,-1,-1] output 1 