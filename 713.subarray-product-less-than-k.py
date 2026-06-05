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


        # # mehtod 3: sliding window; O(n) time; O(1) space 
        
        # res = 0

        # l = 0

        # cum_prod = 1

        # for r in range(len(nums)):

        #     cum_prod *= nums[r]

        #     while l <= r and cum_prod >= k: # Make sure we never shrink past the right pointer l <= r

        #         cum_prod //= nums[l]        # /= integer //= float

        #         l += 1

        #     # Count all valid subarrays ending at r and add at once 
        #     res += (r - l + 1) # res += 1

        # return res


        # mehtod 3: sliding window (move edge case outside); O(n) time; O(1) space 

        if k <= 1: 

            return 0
        
        res = 0

        l = 0

        cum_prod = 1

        for r in range(len(nums)):

            cum_prod *= nums[r]

            while cum_prod >= k: 

                cum_prod //= nums[l]         # /= integer //= float

                l += 1

            # Count all valid subarrays ending at r and add at once 
            res += (r - l + 1) # res += 1

        return res


# @lc code=end


# After the while loop finishes, nums[l:r+1] is the LONGEST valid window ending at r whose 
# product is < k. Therefore, every subarray ending at r and starting anywhere from l to r 
# is also valid: 
# [r]
# [r-1, r]
# [r-2, r]
# ...
# [l, ..., r]
#
# Number of valid subarrays ending at r: r - l + 1. Then, we add all of them at once before 
# r advances.


# e.g., 

# nums = [10, 5, 2, 6], k = 100

# r=0 (nums[r]=10), product=10, window=[l=0, r=0] -> [10]
# subarrays ending at r=0:
#     [10]       -> product 10  < 100 
# r - l + 1 = 0 - 0 + 1 = 1
# res += 1  → res=1

# r=1 (nums[r]=5), product=50, window=[l=0, r=1] -> [10, 5]
# subarrays ending at r=1:
#     [5]        -> product 5   < 100 
#     [10, 5]    -> product 50  < 100 
# r - l + 1 = 1 - 0 + 1 = 2
# res += 2  → res=3

# r=2 (nums[r]=2), product=100, 100 >= 100 so shrink:
#     product //= nums[0]=10  → product=10, l=1
#     window=[l=1, r=2] -> [5, 2]
# subarrays ending at r=2:
#     [2]        -> product 2   < 100 
#     [5, 2]     -> product 10  < 100 
# r - l + 1 = 2 - 1 + 1 = 2
# res += 2  → res=5

# r=3 (nums[r]=6), product=60, window=[l=1, r=3] -> [5, 2, 6]
# subarrays ending at r=3:
#     [6]        -> product 6   < 100 
#     [2, 6]     -> product 12  < 100 
#     [5, 2, 6]  -> product 60  < 100 
# r - l + 1 = 3 - 1 + 1 = 3
# res += 3  → res=8