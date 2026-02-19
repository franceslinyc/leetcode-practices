#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        this_set = set()

        res = 0

        # Similar to LC 76; l to shrink, r to expand

        l = 0
        
        for r in range(len(s)): 

            while s[r] in this_set:    # Careful! Keep shrinking window until all duplicates are removed

                this_set.remove(s[l])  # Remove lefmost character

                l += 1
            
            # Add
            this_set.add(s[r])

            # Update result 
            res = max(res, r - l + 1)

        return res 


# a b c a b c b b
#  
# a b c   res = 3
# b c a   res = 3
# c a b   res = 3
# a b c   res = 3
# c b     res = 2
# b       res = 1

        
# @lc code=end

