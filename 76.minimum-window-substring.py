#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "": 

            return ""
        
        this_count, this_window = {}, {} # Store freq of characters in t and freq of characters in current window of s, respectively

        for i in range(len(t)): 

            this_count[t[i]] = 1 + this_count.get(t[i], 0)

        res, res_length = [-1, -1], float("infinity") 

        have, need = 0, len(this_count)  # Store how many characters that match required freq and **unique** characters we need to match
                                         # Careful! Not need = len(t)

        # Similar to LC 3

        l = 0 

        # Expand the window via r; l to shrink, r to expand

        for r in range(len(s)): 

            this_window[s[r]] = 1 + this_window.get(s[r], 0)

            if s[r] in this_count and this_window[s[r]] == this_count[s[r]]: 

                have += 1

            while have == need:  # Keep updating and shrinking while the window is valid

                # Update result if this window is smaller 

                if (r - l + 1) < res_length: 

                    res = [l, r] # Both inclusive

                    res_length = (r - l + 1)

                # Shrink the window via l

                this_window[s[l]] -= 1 # Remove leftmost character 

                # Check if we break validity
                
                if s[l] in this_count and this_window[s[l]] < this_count[s[l]]: 

                    have -= 1
                
                # Move left pointer 

                l += 1

        l, r = res 

        return s[l: r + 1] if res_length != float("infinity") else ""
    
        # s[start: end] start inclusive; end is not

        
# s is the search space; t is the reference
# Careful! use r to expand; use l to shrink        

# Idea: 
# Expand window (r += 1)
# Try to make it valid
# Once valid -> enter while have == need
# Shrink from left (l += 1)
# Eventually break validity (have -= 1)
# Exit loop
# Go back to expanding (r += 1)

# @lc code=end

