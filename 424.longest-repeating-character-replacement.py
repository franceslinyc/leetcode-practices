#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # # method 1 sliding window: O(m * n) time, m is total # of unique character, n is length of string; O(m) space
        
        # res = 0

        # this_set = set(s)

        # for c in this_set: 

        #     count = 0

        #     l = 0

        #     for r in range(len(s)): 

        #         if s[r] == c: 

        #             count += 1
            
        #         while (r - l + 1) - count > k:  # Keep shrinking window from left if too many replacements needed

        #             if s[l] == c: 

        #                 count -= 1

        #             l += 1           # Always move the left pointer 

        #         res = max(res, r - l + 1)       # Otherwise the window is valid, i.e., (r - l + 1) - count <= k

        # return res


        # method 2 sliding window, optimial: O(n) time, where n is length of string; O(m) space, where m is total # of unique character
      
        res = 0 

        this_map = {}

        highest_freq = 0 

        l = 0 

        for r in range(len(s)): # Or while r < len(s) for r = 0

            this_map[s[r]] = this_map.get(s[r], 0) + 1

            highest_freq = max(highest_freq, this_map[s[r]])
            
            # The window remains valid as long as the number of characters to replace
            # (i.e., window size - frequency of the most common character) is <= k.
            # <=> When condition is broken, shrink the window.  
            
            while (r - l + 1) - highest_freq > k: 

                this_map[s[l]] -= 1

                l += 1

            res = max(res, r - l + 1)

        return res


# We can use a sliding window with a frequency map to track character counts. The window is 
# valid as long as the number of replacements needed does not exceed k, i.e., 
# (window size - frequency of the most common character) <= k. This value represents how many 
# characters in the current window must be replaced to make all characters the same. This 
# runs in O(n) time since both pointers move at most once, and uses O(m) space, where m is
# size of the character map. 


# @lc code=end

