#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # method 1: horizontal scanning; time O(n * m), n: length of shortest string, m: # of string, space O(1)
        
        res = ""

        for i in range(len(strs[0])):         # Check character index, i.e., i = 0, ..., 5 for "flower"

            for j in range(len(strs)):        # Check every string

                if i == len(strs[j]) or strs[0][i] != strs[j][i]: # Return res if any string is too short or has a different character at index i

                    return res
       
            # for s in strs:                  # "flower", "flow", "flight"       
                
            #     if i == len(s) or strs[0][i] != s[i]: 

            #         return res
            
            res += strs[0][i]     # Verify that all strings at that character index first (i.e., outside j loop), then add. 

        return res


        # method 2: vertical scanning 


# Outer loop loops through each character index for the first string
# Inner loop checks for all strings at the same character index 
# Not exactly but close: 
# i = 0
# Check "f" = "f" = "f"
# Add to res
# i = 1
# Check "l" = "l" = "l"
# Add to res
# i = 2
# Check "o" = "o" != "i"
# Do not add


# @lc code=end

