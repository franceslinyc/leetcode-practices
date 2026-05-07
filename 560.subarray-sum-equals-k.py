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

        #     current_prefix_sum = 0

        #     # Loop through subarray from i to each j -> nums[i....j]
            
        #     for j in range(i, len(nums)):

        #         current_prefix_sum += nums[j]

        #         # Increment res if the current prefix sum is equal to k
                
        #         if current_prefix_sum == k: 

        #             res += 1

        # return res
        

        # method 2: Hash Map; O(N) time; O(N) space

        res = 0 

        prefix_sum_map = {0:1} #{}

        current = 0   # current_prefix_sum

        for num in nums: 

            current += num

            # Increment res if a subarray with sum k exists

            prev = current - k

            if prev in prefix_sum_map: 

                res += prefix_sum_map[prev]

            prefix_sum_map[current] = prefix_sum_map.get(current, 0) + 1

        return res


# We use a running prefix sum and a hashmap to store the frequency of each prefix sum. 
# For each element, we check how many times previous prefix sum (current prefix sum - k) 
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
# need = 1 - k = 1 - 2 = -1 Not seen in map-> Do not update res
# prefix_sum_map = {0:1, 1:1} Always add current_prefix_sum:count to map

# index = 1, num = -1
# current_prefix_sum = 0
# need = 0 - k = 0 - 2 = -2 Not seen in map-> Do not update res
# prefix_sum_map = {0:2, 1:1} Always add current_prefix_sum:count to map

# index = 2, num = 1
# current_prefix_sum = 1
# need = 1 - k = 1 - 2 = -1 Not seen in map-> Do not update res
# prefix_sum_map = {0:2, 1:2} Always add current_prefix_sum:count to map

# index = 3, num = 1
# current_prefix_sum = 2
# need = 2 - k = 2 - 2 = 0 Seen 2 times in map -> Update res += 2 -> res = 2
# prefix_sum_map = {0:2, 1:2, 2:1} Always add current_prefix_sum:count to map


# @lc code=end

