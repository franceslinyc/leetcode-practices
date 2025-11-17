#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:

        l, r = 0, len(s) - 1

        while l < r: 

            if s[l] != s[r]: 

                skipL = s[l + 1: r + 1] # r + 1 to stop at r
                skipR = s[l: r]         # r to stop at r - 1

                return skipL == skipL[::-1] or skipR == skipR[::-1] # Return False if either is False
            
            l += 1
            r -= 1

        return True


# @lc code=end

