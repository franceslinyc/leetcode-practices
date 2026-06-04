#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # method 1: sliding window: O(n) time ; O(1) space for 26 characters
        
        # Related to LC 438
        
        if len(s1) > len(s2): 

            return False

        s1_count, s2_count = [0] * 26, [0] * 26

        for c in s1: 

            s1_count[ord(c) - ord("a")] += 1

        l = 0

        for r in range(len(s2)): 

            s2_count[ord(s2[r]) - ord("a")] += 1

            if (r - l + 1) > len(s1): # While works but don't need to since the window size is fixed

                s2_count[ord(s2[l]) - ord("a")] -= 1

                l += 1

            if s1_count == s2_count:  # Compare the full array every step; See method 3 for improvement

                return True
        
        return False


        # # method 1-2: sliding window: O(n) time ; O(1) space

        # # Like method 1,  but uses {}, instead of []. 

        # if len(s1) > len(s2): 

        #     return False

        # s1_count, s2_count = {}, {}

        # for c in s1: 

        #     s1_count[c] = s1_count.get(c, 0) + 1

        # l = 0 

        # for r in range(len(s2)): 

        #     s2_count[s2[r]] = s2_count.get(s2[r], 0) + 1

        #     if (r - l + 1) == len(s1): 

        #         if s1_count == s2_count: 

        #             return True
                
        #         s2_count[s2[l]] -= 1

        #         if s2_count[s2[l]] == 0: 

        #             s2_count.pop(s2[l])

        #         l += 1

        # return False


        # method 2: hash map via Neetcode


        # # method 3: sliding window via Neetcode: O(n) time ; O(1) space for 26 characters
        
        # if len(s1) > len(s2):

        #     return False

        # s1_count, s2_count = [0] * 26, [0] * 26

        # for i in range(len(s1)):

        #     s1_count[ord(s1[i]) - ord('a')] += 1

        #     s2_count[ord(s2[i]) - ord('a')] += 1

        # matches = 0

        # for i in range(26):

        #     matches += (1 if s1_count[i] == s2_count[i] else 0)

        # l = 0

        # for r in range(len(s1), len(s2)): # start: len(s1) because the first window has already been processed during initialization

        #     if matches == 26:

        #         return True

        #     # Add one character at the right
            
        #     index = ord(s2[r]) - ord('a')

        #     s2_count[index] += 1

        #     if s1_count[index] == s2_count[index]:

        #         matches += 1

        #     elif s1_count[index] + 1 == s2_count[index]:

        #         matches -= 1

        #     # Remove one character from the left

        #     index = ord(s2[l]) - ord('a')

        #     s2_count[index] -= 1

        #     if s1_count[index] == s2_count[index]:

        #         matches += 1

        #     elif s1_count[index] - 1 == s2_count[index]:

        #         matches -= 1

        #     l += 1

        # return matches == 26


        # # method 4: sliding window via https://www.youtube.com/watch?v=quSfR-uwkZU: O(n) time ; O(1) space for 26 characters

        # if len(s1) > len(s2): 

        #     return False
        
        # s1_count, s2_count = [0] * 26, [0] * 26

        # for i in range(len(s1)):

        #     s1_count[ord(s1[i]) - ord('a')] += 1      

        #     s2_count[ord(s2[i]) - ord('a')] += 1     

        # if s1_count == s2_count:         # Early return                           

        #     return True

        # for i in range(len(s1), len(s2)): 

        #     s2_count[ord(s2[i]) - ord('a')] += 1             # New character entering the window

        #     s2_count[ord(s2[i - len(s1)]) - ord('a')] -= 1   # Character leavig the window

        #     if s1_count == s2_count: 

        #         return True
        
        # return False


# @lc code=end

