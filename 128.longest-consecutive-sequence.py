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


# We use a hash set to allow O(1) lookups and only begins expanding a sequence when the 
# number is a start (i.e., (num - 1) is not in the set). From each starting point, 
# it counts forward to measure the length of the consecutive sequence, ensuring each number 
# is processed at most once. The algorithm runs in O(n) time with O(n) space due to the set.


# @lc code=end

