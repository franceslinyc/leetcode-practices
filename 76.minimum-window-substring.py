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
        
        this_count, this_window = {}, {}

        for c in t: 

            this_count[c] = 1 + this_count.get(c, 0)

        res = [-1, -1] 

        res_len = float("infinity")

        have = 0 

        need = len(this_count) # Careful not len(t)!

        l = 0 

        # Expand the window via r

        for r in range(len(s)): 

            c = s[r]
        
            this_window[c] = 1 + this_window.get(c, 0) # Store all characters

            # If this character is required and its count is now satisfied, increment have. 

            if c in this_count and this_window[c] == this_count[c]: 
            
                have += 1

            # # For understanding purpose 

            # this_window[s[r]] = 1 + this_window.get(s[r], 0) 

            # if s[r] in this_count and this_window[s[r]] == this_count[s[r]]: 

            #     have += 1

            while have == need:  # Update and shrink when the window is valid

                # Update

                if (r - l + 1) < res_len: 

                    res = [l, r] # Both inclusive

                    res_len = (r - l + 1)

                # Shrink the window via l

                this_window[s[l]] -= 1 # Remove leftmost character 

                if s[l] in this_count and this_window[s[l]] < this_count[s[l]]: 

                    have -= 1

                l += 1

        l, r = res 

        return s[l: r + 1] if res_len != float("infinity") else ""
    
        # s[start: end] start inclusive; end is not

        
# s is the search space; t is the reference
# Careful! use r to expand; use l to shrink        


# @lc code=end

