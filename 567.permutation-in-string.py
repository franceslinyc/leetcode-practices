#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # method 1: sliding window: O(n) time ; O(1) space for 26 characters
        
        if len(s1) > len(s2): 

            return False

        s1_count, s2_count = [0] * 26, [0] * 26

        for c in s1: 

            s1_count[ord(c) - ord("a")] += 1

        l = 0

        for r in range(len(s2)): 

            s2_count[ord(s2[r]) - ord("a")] += 1

            if (r - l + 1) > len(s1): # while works but not necessary since the window size is fixed

                s2_count[ord(s2[l]) - ord("a")] -= 1

                l += 1

            if s1_count == s2_count: 

                return True

        # method 2: hash map via Neetcode

        # method 3: sliding window via Neetcode

        # method 4: sliding window via https://www.youtube.com/watch?v=quSfR-uwkZU

        return False

        
# @lc code=end

