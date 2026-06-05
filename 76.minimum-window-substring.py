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
        
        t_count, w_count = {}, {} # Store freq of characters in t and freq of characters in current window of s, respectively

        for c in t: 

            t_count[c] = t_count.get(c, 0) + 1

        res, res_length = [-1, -1], float("infinity") 

        have, need = 0, len(t_count)  # Store how many characters that match required freq and **unique** characters we need to match
                                      # Careful! Not need = len(t)

        # Similar to LC 3

        l = 0 

        for r in range(len(s)): 

            w_count[s[r]] = w_count.get(s[r], 0) + 1
            
            if s[r] in t_count and w_count[s[r]] == t_count[s[r]]:    # Check validity, i.e., If s[r] is in t_count and its count in w_count matches t_count, increment have.

                have += 1

            while have == need:  # Keep updating and shrinking while the window is valid

                # Update result if this window is smaller 

                if (r - l + 1) < res_length: 
                                                                                                                                                                                                                                         
                    res = [l, r] # Both inclusive

                    res_length = (r - l + 1)

                # Shrink the window via l to find the smallest valid window: Remove from window, update validity, and move left pointer 

                # Like LC 209 except we add a if() here

                w_count[s[l]] -= 1            # Careful! Don't forget 
                
                if s[l] in t_count and w_count[s[l]] < t_count[s[l]]:  # Update validity if we break it

                    have -= 1

                l += 1

        l, r = res     # Retrieve the best window found once the outer for loop is done running

        return s[l: r + 1] if res_length != float("infinity") else ""
    
        # Careful! s[start: end] start inclusive; end is not
        # Careful! string uses :, e.g., string[start: end]


# @lc code=end


# We can use a sliding window with two hash maps to track required character counts and the 
# current window, expanding the right pointer and shrinking from the left when all requirements 
# are met to maintain the minimum valid substring. The time complexity is O(n) since each 
# character is visited at most twice, and the space complexity is O(m) where m is the number 
# of unique characters in s and t.
 
 
# Idea: 

# Expand window (r += 1)
# Try to make it valid
# Once valid -> enter while have == need
# Shrink from left (l += 1) to find the smallest valid window
# Eventually break validity (have -= 1)
# Exit loop
# Go back to expanding (r += 1)


# e.g., 

# s = "ADOBECODEBANC"
# t = "ABC"

# t_count = {'A': 1, 'B': 1, 'C': 1}
# need = 3   # Must satisfy A, B, and C
# have = 0

# r hits 
# 'A':  w_count = {'A':1}          
# A in t_count AND w_count['A'] == t_count['A'] = 1 -> have=1
# 'D':  w_count = {'A':1,'D':1}                              
# D not in t_count                                  -> have=1
# 'O':  w_count = {'A':1,'D':1, 'O':1}                       
# O not in t_count                                  -> have=1
# 'B':  w_count = {'A':1, 'D':1, 'O':1, 'B':1}               
# B in t_count AND w_count['B'] == t_ount['B'] = 1  -> have=2
# 'E':  w_count = {'A':1, 'D':1, 'O':1, 'B':1, 'E':1}        
# E not in t_count                                  -> have=2
# 'C':  w_count = {'A':1, 'D':1, 'O':1, 'B':1, 'E':1, 'C':1} 
# C in t_count AND w_count['C'] == t_count['C'] = 1 -> have=3 