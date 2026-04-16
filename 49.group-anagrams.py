#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # method 1 hash map: O(M*N) time, M: length of a string, N: #s of strings in strs; O(M*N) space for output list 
        
        res = defaultdict(list) # Instead of {}, handle edge case where a dictionary key is accessed before it exists. 
                                # Default dict with a list; 
                                # Initialize res[tuple(count)] = [] automatically
        for s in strs: 

            count = [0] * 26

            # Build frequency count for this word

            for c in s: 

                count[ord(c) - ord("a")] += 1
            
            # Use this frequency count as a dictionary key, and use it to group all anagrams together.

            res[tuple(count)].append(s) # res[count].append(s) won't work; list cannot be key in dict, but tuple can.

        return list(res.values())       # Otherwise, res.values() return a dict, not list


# Idea:
# 
# We use a hash map where the key is a tuple (of the 26-character count) and the value is 
# a list of strings. For each string, we compute its character frequency and use that tuple 
# as the key to group anagrams together. The solution is O(MN) time because we process N 
# strings and scan up to M characters per string, and O(MN) space because all N strings 
# are stored in the hashmap groups and each string can be up to M long in the worst case.
#
# Examples: 
# 
#        A B C D E ...
# count [1 1 1 ...... ] for "abc"   
# count [1 1 1 ...... ] for "bca"   
# count [1 1 0 1..... ] for "abd"  


# @lc code=end

