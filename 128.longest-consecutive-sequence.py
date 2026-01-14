#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        this_set = set(nums)

        max_length = 0

        for num in this_set: # for num in nums: Loop through unique values only; Otherwise time limit exceed O(n^2) 

            if (num - 1) not in this_set:         # Check if it is the starting number

                length = 1

                while (num + length) in this_set: # Careful not num + 1

                    length += 1

                max_length = max(length, max_length)
            
        return max_length


# nums = [100,4,200,1,3,2]
# output = 4
# Idea: 
# 100 is a start   -> 101 not there -> length = 1
# 4 is not a start
# 200 is a start   -> 201 not there -> length = 1 
# 1 is a start     -> 2 is there -> length += 1  -> -> ->
# 3 is not a start
# 2 is not a start 


# @lc code=end

