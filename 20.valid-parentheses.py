#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:

        this_map = {")": "(", "]": "[", "}": "{"}

        this_stack = []

        for i in range(len(s)): # or for c in s: 

            if s[i] not in this_map: 

                this_stack.append(s[i])

            else: 

                if not this_stack or this_stack[-1] != this_map[s[i]]:

                    return False

                this_stack.pop()                    

        return not this_stack  # return True if empty 

# @lc code=end

