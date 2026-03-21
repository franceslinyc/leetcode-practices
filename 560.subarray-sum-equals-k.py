#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # # method 1: Brute Force; O(N^2) time; O(1) space

        # res = 0

        # for i in range(len(nums)):

        #     sum = 0

        #     for j in range(i, len(nums)):

        #         sum += nums[j]

        #         if sum == k:

        #             res += 1

        # return res
        

        # method 2: Hash Map; O(N) time; O(N) space

        res = 0 

        current_prefix_sum = 0 

        prefix_sum_map = {0:1} 

        for num in nums: 

            current_prefix_sum += num

            diff = current_prefix_sum - k        # prefix[j] - prefix[i] = k <=> prefix[i] = prefix[j] - k

            if diff in prefix_sum_map: 

                res += prefix_sum_map[diff]

            prefix_sum_map[current_prefix_sum] = prefix_sum_map.get(current_prefix_sum, 0) + 1

        return res


# We use a running prefix sum and a hashmap to store the frequency of each prefix sum. 
# For each element, we check how many times previous prefix sums (current prefix sum - k) 
# has occured, which tells us how many subarrays ending at the current index sum to k. This
# gives us O(N) time since we traverse the array once, and O(N) space since we store prefix
# sums in the hashmap. 




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


# @lc code=end

