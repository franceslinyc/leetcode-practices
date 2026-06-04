#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # method 1 DFS + Cycle Detection: O(V + E) time; O(V + E) space, where V is the # of courses and E is the # of prerequisites.

        # prereq_map = {i: [] for i in range(numCourses)}

        prereq_map = defaultdict(list) # faster 

        for crs, pre in prerequisites:

            prereq_map[crs].append(pre)

        res = []

        path, visit = set(), set()

        def dfs(crs):

            if crs in path:         # Cycle detected -> False 

                return False

            if crs in visit:        # Already processed -> True

                return True

            # Go deeper

            path.add(crs)

            for pre in prereq_map[crs]:

                if not dfs(pre):     # Recursively run dfs on course's prerequisite's prerequisite's prerequisite's... till prerequisite is in visit (base case).

                    return False

            path.remove(crs)

            visit.add(crs)     # Avoid revisit; Cannot overwrite because we need it to build res

            res.append(crs)

            return True

        for c in range(numCourses):

            if not dfs(c): 

                return []

        return res        


        # method 2: topological sort (Kahn's Algorithm)

        # method 3: topological sort (DFS)


# @lc code=end

# LC 145 postorder DFS on tree may help! 

# prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# prereq_map = 
# crs pre
# 1   [0]
# 2   [0]
# 3   [1, 2]

# dfs: 3 -> 1 -> 0
# dfs: 3 -> 2 -> 0 (already cleared)

# dfs(3)          path={3}
#   dfs(1)        path={3,1}
#     dfs(0)      path={3,1,0}
#                 ✓ base → append(0), path={3,1},   visit={0},     res=[0]
#   ← backtrack(1)→ append(1),        path={3},     visit={0,1},   res=[0,1]
#   dfs(2)        path={3,2}
#     dfs(0)      ✓ in visit → skip
#   ← backtrack(2)→ append(2),        path={3},     visit={0,1,2}, res=[0,1,2]
# ← backtrack(3)  → append(3),        path={},      visit={0,1,2,3}, res=[0,1,2,3]