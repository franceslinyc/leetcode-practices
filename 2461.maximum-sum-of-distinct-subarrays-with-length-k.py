#
# @lc app=leetcode id=2461 lang=python3
#
# [2461] Maximum Sum of Distinct Subarrays With Length K
#

# @lc code=start
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        # method: O(n) time, where n is the length of nums; O(k) space, since the map stores at most k distinct values at any given time

        res = 0

        this_map = {} 

        cum_sum = 0

        l = 0 

        for r in range(len(nums)): 

            this_map[nums[r]] = this_map.get(nums[r], 0) + 1

            cum_sum += nums[r]

            # Similar to LC 567, 438, but especially the commented part of 438

            if (r - l + 1) > k: 

                this_map[nums[l]] -= 1

                if this_map[nums[l]] == 0: 

                    this_map.pop(nums[l])

                cum_sum -= nums[l]

                l += 1

            if (r - l + 1) == k and len(this_map) == k: 

                res = max(res, cum_sum)

        return res

        
# @lc code=end

