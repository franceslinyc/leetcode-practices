#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        # method 1: brute force via Neetcode


        # method 2: prefix count + sliding window via Neetcode: O(n + m) time; O(m) space, where n is the length of the string s, and m is the length of the string p


        # # method 3: sliding window via Neetcode: O(n + m) time, where n is the length of the string s, and m is the length of the string p; O(1) space

        # if len(p) > len(s): 

        #     return []

        # s_count, p_count = {}, {}

        # # build frequency maps for first window / substring

        # for i in range(len(p)): 

        #     p_count[p[i]] = p_count.get(p[i], 0) + 1

        #     s_count[s[i]] = s_count.get(s[i], 0) + 1

        # # check first window

        # res = [0] if p_count == s_count else []

        # l = 0 

        # for r in range(len(p), len(s)): # Because we already take care of the first window

        #     s_count[s[r]] = s_count.get(s[r], 0) + 1 # add new right character

        #     s_count[s[l]] -= 1                       # remove left character

        #     if s_count[s[l]] == 0: # Need this clean up the hashmap

        #         s_count.pop(s[l])

        #     l += 1   # Always move l pointer forward

        #     #r+= 1   # Always move r pointer forward; If we use while loop, instead of for loop

        #     if p_count == s_count: 

        #         res.append(l)
        
        # return res


        # method 3-1: sliding window, variation: O(n + m) time, where n is the length of the string s, and m is the length of the string p; O(1) space

        # Mimic LC 567

        if len(p) > len(s): 

            return []

        s_count, p_count = [0] * 26, [0] * 26

        for c in p: 

            p_count[ord(c) - ord('a')] += 1

        res = []
        
        l = 0 

        for r in range(len(s)): 

            s_count[ord(s[r]) - ord('a')] += 1

            # if (r - l + 1) > len(p):      # Keep window size equal to len(p)

            #     s_count[ord(s[l]) - ord('a')] -= 1

            #     l += 1            
        
            # if s_count == p_count: 

            #     res.append(l)

            if (r - l + 1) == len(p): 

                if s_count == p_count: 

                    res.append(l)

                s_count[ord(s[l]) - ord('a')] -= 1

                l += 1

        return res


        # method 3-2: sliding window, variation: O(n + m) time, where n is the length of the string s, and m is the length of the string p; O(1) space

        # Like method 3-1 above, but uses {}, instead of []. 

        # if len(p) > len(s): 

        #     return []

        # s_count, p_count = {}, {}

        # for c in p: 

        #     p_count[c] = p_count.get(c, 0) + 1

        # res = []

        # l = 0 

        # for r in range(len(s)): 

        #     s_count[s[r]] = s_count.get(s[r], 0) + 1

        #     if (r - l + 1) == len(p): # Careful! Not len(s_count) == len(p_count), which count # of keys.  

        #         if s_count == p_count: 

        #             res.append(l)

        #         s_count[s[l]] -= 1

        #         if s_count[s[l]] == 0: # Careful! Need to clean up the map.

        #             s_count.pop(s[l])

        #         l += 1

        # return res


        # method 4: sliding window, optimal 


# @lc code=end


# We can use a sliding window with two frequency arrays of size 26 to track character counts
# in s and p. The window is valid as long as both frequency arrays are equal, i.e.,
# s_count == p_count. We expand the window by adding s[r], shrink from the left whenever
# the window exceeds len(p), then check for a match. This runs in O(n + m) time where n
# and m are the lengths of s and p, and uses O(1) space since both arrays are fixed size 26.