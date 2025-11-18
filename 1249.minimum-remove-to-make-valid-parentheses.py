#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#

# @lc code=start
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        res = []

        count = 0 

        for c in s: 

            if c == "(": 

                res.append(c)

                count += 1

            elif c == ")" and count > 0: 

                res.append(c)

                count -= 1

            elif c != ")": 

                res.append(c)

        filtered = []

        for c in res[::-1]: 

            if c == "(" and count > 0: 

                count -= 1

            else: 

                filtered.append(c)

        return "".join(filtered[::-1])
        
# @lc code=end

