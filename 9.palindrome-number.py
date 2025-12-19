#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0: 

            return False
        
        div = 1

        while x >= div * 10: 

            div *= 10

        while x: 

            right = x % 10

            left = x // div
        
            if right != left: 

                return False
            
            x = (x % div) // 10  

            div = div // 100 # Remove 2 digits (1 for left; 1 for right)
            
        return True
        
# 1221
# 1221 % 1000 = 221
# 221 // 10   = 22


# @lc code=end

