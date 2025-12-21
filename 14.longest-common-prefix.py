#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        res = ""

        for i in range(len(strs[0])):         # i = 0, ..., 5 for "flower"

            # for j in range(len(strs)):      # Just for understanding purpose

            #     if i == len(strs[j]) or strs[0][i] != strs[j][i]: 
       
            for s in strs:                    # "flower", "flow", "flight"

                if i == len(s) or strs[0][i] != s[i]: 

                    return res
            
            res += strs[0][i]

        return res


# Outer loop controls the character position
# Inner loop checks for all strings at the same position 
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

