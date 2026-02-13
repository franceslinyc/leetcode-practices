#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:  
               
        l, r = 0, len(s) - 1

        while l < r:             # l < r for comparing mirrored characters 

            while l < r and not s[l].isalnum(): # Move l forward untill it points to an alphanumeric character

                l += 1

            while r > l and not s[r].isalnum(): # Move r backward

                r -= 1

            if s[l].lower() != s[r].lower():

                return False
            
            l += 1
            r -= 1

        return True
    

        # Not recommended; Extra time and space
        
        # new_s = ""

        # for i in range(len(s)): 

        #     if s[i].isalnum(): 

        #         new_s += s[i].lower()

        # l, r = 0, len(new_s) - 1

        # while l < r: 

        #     if new_s[l] != new_s[r]: 

        #         return False
            
        #     l += 1
        #     r -= 1

        # return True


# @lc code=end

