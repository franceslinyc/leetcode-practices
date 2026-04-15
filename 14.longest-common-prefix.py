#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # method 1: horizontal scanning; time O(n * m), n: length of shortest string, m: # of string, space O(1)

        # method 2: vertical scanning ; time O(n * m), n: length of shortest string, m: # of string, space O(1)

        res = ""

        for i in range(len(strs[0])):         # Check character index, i.e., i = 0, ..., 5 for "flower"

            for j in range(len(strs)):        # Check every string

                if i == len(strs[j]) or strs[0][i] != strs[j][i]: # Return res if any string is too short or has a different character at index i

                    return res
       
            # for s in strs:                  # "flower", "flow", "flight"       
                
            #     if i == len(s) or strs[0][i] != s[i]: 

            #         return res
            
            res += strs[0][i]     # Verify that all strings at that character index first (i.e., outside j loop), 
                                  # then add. 

        return res 


# We iterate through each character index of the first string and, for each index, 
# checks all other strings to ensure the characters match. If a mismatch is found 
# or any string ends, it returns the prefix built so far. Otherwise, it appends 
# the matching character to the result. The time complexity is O(N*M), where N is 
# the length of the shortest string and M is the number of strings, and the space 
# complexity is O(1). (res is O(N) space but output is excluded from space complexity). 


# e.g., strs = ["flower", "flow", "flight"]

#       i  0   1   2   3   4 ...
# j 
# 0        f   l   o   w   e   r
# 1        f   l   o   w
# 2        f   l   i   g   h   t

# for i in range(len(strs[0])):        # Go character by character (Fix col)
#     for j in range(len(strs)):       # Check all strings (Check for all rows)


# @lc code=end

