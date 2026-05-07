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

        prefix_sum_map = {0:1} #{}

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

# e.g., 
# [1, -1, 1, 1, 1, 1]   k = 2

# current_prefix_sum = 0
# prefix_sum_map = {0:1} Without this, index = 3 won't work.
# res = 0

# index = 0, num = 1
# current_prefix_sum = 1
# need = 1 - k = 1 - 2 = -1 Not seen -> Do not update res
# prefix_sum_map = {0:1, 1:1}

# index = 1, num = -1
# current_prefix_sum = 0
# need = 0 - k = 0 - 2 = -2 Not seen -> Do not update res
# prefix_sum_map = {0:2, 1:1}

# index = 2, num = 1
# current_prefix_sum = 1
# need = 1 - k = 1 - 2 = -1 Not seen -> Do not update res
# prefix_sum_map = {0:2, 1:2}

# index = 3, num = 1
# current_prefix_sum = 2
# need = 2 - k = 2 - 2 = 0 Seen 2 times -> res += 2 -> res = 2
# prefix_sum_map = {0:2, 1:2, 2:1}


# @lc code=end

