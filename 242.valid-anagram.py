#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # method 1 hash map: O(n + m) time; O(1) space

        if len(s) != len(t): 

            return False
        
        s_dict = {} # Or defaultdict(int)
        t_dict = {} # Or defaultdict(int)
        
        for i in range(len(s)): 
            
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1

            t_dict[t[i]] = t_dict.get(t[i], 0) + 1
        
        return s_dict == t_dict

        # # method 2 hash map (array): O(n + m) time; O(1) space

        # if len(s) != len(t):
        #     return False

        # count = [0] * 26
        # for i in range(len(s)):
        #     count[ord(s[i]) - ord('a')] += 1
        #     count[ord(t[i]) - ord('a')] -= 1

        # for val in count:
        #     if val != 0:
        #         return False
        # return True

        
# @lc code=end

