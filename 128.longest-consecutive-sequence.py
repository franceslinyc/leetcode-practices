#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # method 1: hash set: time O(n), space O(n)
        
        this_set = set(nums) 

        max_length = 0

        for num in this_set: # Loop through unique values only to prevent O(n^2) 
                             # Set is iterable, but it is NOT indexable 

            if (num - 1) not in this_set:         # Check if it is the starting number

                length = 1

                while (num + length) in this_set: # Careful not num + 1

                    length += 1

                max_length = max(length, max_length)
            
        return max_length


        # method 2: hash map 


# nums = [100,4,200,1,3,2]
# nums = {100,4,200,1,3,2}
# output = 4
# Idea: 
# 99 not there  -> 100 is a start -> but 101 is not -> Calculate max length
# 4 is not a start
# 199 not there -> 200 is a start -> but 201 is not -> Calculate max length
# 0 not there   -> 1 is a start   -> 2 is -> Increment length -> 3 is -> 4 is -> but 5 is not -> Calculate max length
# 3 is not a start
# 2 is not a start 


# @lc code=end

