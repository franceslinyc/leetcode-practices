#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        this_set = set(s)

        res = 0

        for c in this_set: 

            count = 0

            l = 0

            for r in range(len(s)): 

                if s[r] == c: 

                    count += 1
            
                while (r - l + 1) - count > k:  # Keep shrinking window from left if too many replacements needed

                    if s[l] == c: 

                        count -= 1

                    l += 1           # Always move the left pointer 

                res = max(res, r - l + 1)       # Otherwise the window is valid, i.e., (r - l + 1) - count <= k

        return res


# AABABBA

# Initialize the set, i.e., this_set = {'A', 'B'}
# Outer loop loops through each character in the set 
# Inner loop expands the window one character at a time, from left to right


# @lc code=end

