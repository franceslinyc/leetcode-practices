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

        # Maps: prefix sum -> count (how many times we've seen it so far)
        
        prefix_sum_map = {0:1} #{} # Without this initialization, subarrays where prefix sum == k from the beginning will not be counted 

        res = 0 

        current = 0                       # current: current_prefix_sum

        for num in nums: 

            current += num

            # Key idea: 
            # current - (sum of elements BEFORE that subarray) = k
            # <=> sum of elements BEFORE that subarray = current - k

            prev = current - k            # prev: prev_prefix_sum

            # Increment res if a subarray with sum k exists

            if prev in prefix_sum_map: 

                res += prefix_sum_map[prev]

            # Record the current running total after the lookup

            prefix_sum_map[current] = prefix_sum_map.get(current, 0) + 1

        return res


# @lc code=end


# We use a running prefix sum and a hashmap to store the frequency of each prefix sum. 
# For each element, we check how many times previous prefix sum (current prefix sum - k) 
# has occured, which tells us how many subarrays ending at the current index sum to k. This
# gives us O(N) time since we traverse the array once, and O(N) space since we store prefix
# sums in the hashmap. 


# e.g., 
# [1, -1, 1, 1, 1, 1]   k = 3

# prefix sum count
#        0  1

# sum = 1 -> 1 - k = 1 - 3 = -2 but -2 not in prefix_sum_map so add to map
#            (add the current sum 1, not -2)
# res = 0

# prefix sum count
#         0  1
#         1  1

# sum = 1 + (-1) = 0 -> 0 - k = 0 - 3 = -3 but -3 not in prefix_sum_map so add to map
#            (add the current sum 0, so its count goes from 1 to 2)
# res = 0

# prefix sum count
#         0  2
#         1  1

# sum = 1 + (-1) + 1 = 1 -> 1 - k = 1 - 3 = -2 but -2 not in prefix_sum_map so add to map
#            (add the current sum 1, so its count goes from 1 to 2)
# res = 0

# prefix sum count
#         0  2
#         1  2 

# sum = 1 + (-1) + 1 + 1 = 2 -> 2 - k = 2 - 3 = -1 but -1 not in prefix_sum_map so add to map
#            (add the current sum 2)
# res = 0

# prefix sum count
#         0  2
#         1  2  
#         2  1  

# sum = 3 -> 3 - k = 3 - 3 = 0, yes, 
# res += 2 = 2
# (the two earlier 0s are the empty prefix and the prefix after index 1)
# then add the current sum 3 to the map

# prefix sum count
#         0  2
#         1  2
#         2  1
#         3  1

# sum = 4 -> 4 - k = 4 - 3 = 1, yes, 
# res += 2 = 4 
# then add the current sum 4 to the map

# prefix sum count
#         0  2
#         1  2
#         2  1
#         3  1
#         4  1

# return res = 4