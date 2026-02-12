#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list) # Instead of {}, handle edge case where a dictionary key is accessed before it exists. 
                                # Initialize res[tuple(count)] = [] automatically

        for s in strs: 

            count = [0] * 26

            for c in s: 

                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s) # res[count].append(s) won't work; list cannot be key in dict

        return list(res.values())       # Otherwise, res.values() return a dict, not list


# eat 
# count = a b c d e f g ... t
#       =[1 0 0 0 1 0 0 ... 1]        


# @lc code=end

