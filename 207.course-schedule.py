#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # method 1 DFS + Cycle Detection: O(V + E) time; O(V + E) space, where V is the # of courses and E is the # of prerequisites.
        
        prereq_map = {i: [] for i in range(numCourses)}  # Store course: prerequisite
                                                         # {0: [], 1: [], ...}

        for crs, pre in prerequisites:

            prereq_map[crs].append(pre)

        path = set()

        def dfs(crs): # crs: current course

            # ASK: What does "can I finish course crs"?

            # base case #1

            if crs in path:           # Cycle detected -> False

                return False 

            # base case #2

            if prereq_map[crs] == []:  # No prerequisite left -> True

                return True

            # ASK: Can I finish the prerequisite?

            # Go deeper
            
            path.add(crs)

            for pre in prereq_map[crs]: 

                if not dfs(pre):     # Recursively run dfs on **prerequisite**

                    return False

            path.remove(crs)

            prereq_map[crs] = []     # Avoid revisit

            return True

        # Run dfs on **course**

        for c in range(numCourses): 

            if not dfs(c): 

                return False

        return True        


# dfs(crs):
#     1. Is crs in path?       
#     2. Is prereq_map[crs] == []? 
#     3. Otherwise, loop through prereqs, call dfs(pre) on each
#                   └─ dfs(pre):
#                          1. Is pre in path?
#                          2. Is prereq_map[pre] == []?
#                          3. otherwise: loop through pre's prereqs...
#                                        └─ dfs(pre's pre):
#                                               1. ...
#                                               2. ...
#                                               3. ...

# e.g., 
# prerequisites = [[0,1],[0,2],[1,3],[1,4],[3,4]]
# prereq_map = 
# crs pre
# 0   [1,2]
# 1   [3,4]
# 2   []
# 3   [4]
# 4   []

# dfs: 0 -> 1 -> 3 -> 4
# dfs: 0 -> 2

# e.g., 
# prerequisites = [[0,1],[1,2],[2,0]]
# prereq_map = 
# crs pre
# 0   [1]
# 1   [2]
# 2   [0]

# dfs: 0 -> 1 -> 2 -> 0 (Is a cycle)


# @lc code=end

