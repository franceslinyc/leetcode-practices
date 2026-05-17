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

        visiting = set()

        def dfs(crs): # crs: current course

            # base case #1

            if crs in visiting:   # Seen on this path, i.e., detect a cycle

                return False 

            # base case #2

            if prereq_map[crs] == []: # No prerequisite left

                return True

            # Recursively run dfs on **prerequisite**
            
            visiting.add(crs)

            for pre in prereq_map[crs]: 

                if not dfs(pre): 

                    return False

            visiting.remove(crs)

            prereq_map[crs] = []     # Avoid running dfs again 

            return True

        # Recursively run dfs on **course**

        for c in range(numCourses): 

            if not dfs(c): 

                return False

        return True        


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

