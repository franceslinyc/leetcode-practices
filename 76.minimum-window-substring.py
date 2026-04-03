#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # method: sliding window: O(n + m) time, where n is the length of string s, m is the total number of unique characters in
        # string s and t; O(m) space
        
        if t == "": 

            return ""
        
        count_t, count_window = {}, {} # Store freq of characters in t and freq of characters in current window of s, respectively

        for i in range(len(t)): 

            count_t[t[i]] = 1 + count_t.get(t[i], 0)

        res, res_length = [-1, -1], float("infinity") 

        have, need = 0, len(count_t)  # Store how many characters that match required freq and **unique** characters we need to match
                                      # Careful! Not need = len(t)

        # Similar to LC 3

        l = 0 

        # Expand the window via r; l to shrink, r to expand

        for r in range(len(s)): 

            count_window[s[r]] = count_window.get(s[r], 0) + 1
            
            if s[r] in count_t and count_window[s[r]] == count_t[s[r]]:    # Check validity

                have += 1

            while have == need:  # Keep updating and shrinking while the window is valid

                # Update result if this window is smaller 

                if (r - l + 1) < res_length: 
                                                                                                                                                                                                                                         
                    res = [l, r] # Both inclusive

                    res_length = (r - l + 1)

                # Shrink the window via l: Remove from window, update validity, and move left pointer 

                count_window[s[l]] -= 1            # Careful! Don't forget 
                
                if s[l] in count_t and count_window[s[l]] < count_t[s[l]]:  # Update validity if we break it

                    have -= 1

                l += 1

        l, r = res     # Retrieve the best window found

        return s[l: r + 1] if res_length != float("infinity") else ""
    
        # Careful! s[start: end] start inclusive; end is not
        # Careful! string uses :, e.g., string[start: end]


# We can use a sliding window with two hash maps to track required character counts and the 
# current window, expanding the right pointer and shrinking from the left when all requirements 
# are met to maintain the minimum valid substring. The time complexity is O(n) since each 
# character is visited at most twice, and the space complexity is O(m) where m is the number 
# of unique characters in s and t.


# Idea: 

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

