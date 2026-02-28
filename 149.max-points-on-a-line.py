#
# @lc app=leetcode id=149 lang=python3
#
# [149] Max Points on a Line
#

# @lc code=start
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        res = 1

        for i in range(len(points)):

            count = defaultdict(int)

            p1 = points[i]
            
            for j in range(i + 1, len(points)):

                p2 = points[j]

                if p2[0] == p1[0]:

                    slope = float("inf")

                else:

                    slope = (p2[1] - p1[1]) / (p2[0] - p1[0])

                count[slope] += 1

                res = max(res, count[slope] + 1)
                
        return res


# @lc code=end

