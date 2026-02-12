#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for num in nums: 

            count[num] = count.get(num, 0) + 1    # .get retrun value

        freq = [[] for i in range(len(nums) + 1)] # i.e., [[],[],[], ...]

        for num, cnt in count.items():            # .items return key:value pair

            freq[cnt].append(num)

        res = []

        for i in range(len(freq) - 1, 0, -1):     # Careful that start is inclusive; stop is not 

            for num in freq[i]:   # Loop through each num in freq[i]

                res.append(num) 

                if len(res) == k: # Stop immediately when k num are collected

                    return res


# [1, 1, 1, 2, 2, 3]
# count 
# {1: 3, 2: 2, 3: 1} key:value = num:cnt
# freq
# cnt 0  1  2  3  4  5  6
# num   [3][2][1]

# [1, 2, 1, 2, 1, 2, 3, 1, 3, 2]
# count
# {1: 4, 2: 4, 3: 2}
# freq 
# cnt 0  1  2  3  4      5  6  7  8  9  10
# num      [3]   [1,2]
# i.e.,  
#   [[],[],[3],[],[1, 2],[],[],[],[], ...]


# @lc code=end

