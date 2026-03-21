#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        res = 0 

        cum_sum = 0 

        prefix_sum = {0:1}

        for num in nums: 

            cum_sum += num

            diff = cum_sum - k 

            if diff in prefix_sum: 

                res += prefix_sum[diff]

            prefix_sum[cum_sum] = prefix_sum.get(cum_sum, 0) + 1

        return res


# e.g., [1, -1, 1, 1, 1, 1]   k = 2

# prefix_sum = {0:2, # key:value = prefix_sum: count
#               1:2, 
#               2:1,
#               3:1, 
#               4:1}

# Start prefix = {0:1}, cum_sum = 0, res = 0
# Index 0             , cum_sum = 1
# Index 1             , cum_sum = 0
# Index 2             , cum_sum = 1
# Index 3             , cum_sum = 2, diff = 0 in prefix_sum, update res += 2
# Index 4             , cum_sum = 3, diff = 1 in prefix_sum, update res += 2
# Index 5             , cum_sum = 4, diff = 2 in prefix_sum, update res += 1


# We use a running cumulative sum and a hashmap to track how many times each prefix sum 
# has occurred. For each element, we check how many previous sums equal cum_sum - k, 
# which tells us how many subarrays ending here sum to k. Time is O(N) since we traverse 
# the array once, and space complexity is O(N) since we store prefix sums in the hashmap.


# @lc code=end

