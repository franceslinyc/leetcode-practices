#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # method 1 sliding window: O(n) time, where n is length of string; O(m) space, where m is total # of unique character
        
        res = 0

        this_set = set()

        # Similar to LC 76; l to shrink, r to expand

        l = 0
        
        # Expand the window via r; Make sure to check condition BEFORE expanding window 
        
        for r in range(len(s)): 

            while s[r] in this_set:    # Careful! Keep shrinking window until all duplicates are removed

                this_set.remove(s[l])  # Remove lefmost character

                l += 1
            
            this_set.add(s[r])         # Then Add

            res = max(res, r - l + 1)  # Update result 

        return res 


        # method 2: sliding window, optimial: O(n) time, where n is length of string; O(m) space, where m is total # of unique character


# method 1

# We can use a sliding window with a hash set to track characters in the current window. We'd 
# keep expanding the right pointer while characters are unique, and shrink from the left when
# a deplicate appears, and update the max length along the way. This runs in O(n) time since 
# each character is processed at most twice, and O(m) space where m is the size of the character 
# set.


# a b c a b c b b
#  
# a b c   res = 3
# b c a   res = 3
# c a b   res = 3
# a b c   res = 3
# c b     res = 2
# b       res = 1

        
# @lc code=end

