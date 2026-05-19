#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # method 1 DFS + Cycle Detection: O(V + E) time; O(V + E) space, where V is the # of courses and E is the # of prerequisites.

        prereq_map = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:

            prereq_map[crs].append(pre)

        res = []

        visit, path = set(), set()

        def dfs(crs):

            if crs in path:       # Cycle detected -> False 

                return False

            if crs in visit:       # Already processed -> True

                return True

            # Go deeper

            path.add(crs)

            for pre in prereq_map[crs]:

                if dfs(pre) == False:     # Recursively run dfs on **prerequisite**

                    return False

            path.remove(crs)

            visit.add(crs)     # Avoid revisit; Cannot overwrite because we need it to build res

            res.append(crs)

            return True

        for c in range(numCourses):

            if dfs(c) == False:

                return []

        return res        


        # method 2: topological sort (Kahn's Algorithm)

        # method 3: topological sort (DFS)


# @lc code=end

