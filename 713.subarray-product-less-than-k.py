#
# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#

# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        # # method 1: Brute Force; O(N^2) time; O(1) space
        
        # res = 0

        # for i in range(len(nums)):

        #     current_prod = 1

        #     for j in range(i, len(nums)):

        #         current_prod *= nums[j]

        #         if current_prod >= k:

        #             break

        #         res += 1

        # return res


        # method 2: binary search; O(n log n) time; O(n) space


        # mehtod 3: sliding window; O(n) time; O(1) space 
        
        res = 0

        l = 0

        cum_prod = 1

        for r in range(len(nums)):

            cum_prod *= nums[r]

            while l <= r and cum_prod >= k: 

                cum_prod //= nums[l]

                l += 1

            # Count all valid subarrays ending at r and add at once 
            res += (r - l + 1) # res += 1

        return res


# After the while loop finishes, nums[l:r+1] is the LONGEST valid window ending at r
# whose product is < k. Therefore, every subarray ending at r and starting
# anywhere from l to r is also valid: 
# [r]
# [r-1, r]
# [r-2, r]
# ...
# [l, ..., r]
#
# Number of valid subarrays ending at r: r - l + 1. Then, we add all of them at once.


# @lc code=end

