#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # method 1 DFS + Cycle Detection: O(V + E) time; O(V + E) space, where V is the # of courses and E is the # of prerequisites.
        
        # Make adj list to store course: prerequisite
        
        # prereq_map = {i: [] for i in range(numCourses)}  # Store course: prerequisite
        #                                                  # {0: [], 1: [], ...}

        prereq_map = defaultdict(list) # faster 
        
        for crs, pre in prerequisites: # O(V + E) space

            prereq_map[crs].append(pre)

        path = set()                   # Cycle-detection set; O(V) space worst case

        def dfs(crs): # crs: current course

            # ASK: What does "can I finish course crs"?

            # base case #1

            if crs in path:            # Cycle detected -> False

                return False 

            # base case #2

            if prereq_map[crs] == []:  # No prerequisite left -> True

                return True

            # ASK: Can I finish the prerequisite?

            # Go deeper
            
            path.add(crs)

            for pre in prereq_map[crs]: # O(E) total time across ALL calls combined
                
                if not dfs(pre):   # Recursively run dfs on course's prerequisite's prerequisite's prerequisite's... till base cases.
                                     
                    return False

            path.remove(crs)

            prereq_map[crs] = []     # Avoid revisit

            return True

        # Run dfs on all **course**

        for c in range(numCourses): # Run dfs on 0, 1, 2, n-1 in order, with no awareness of the graph structure; O(V) time

            if not dfs(c):          # O(E) total time across ALL calls combined

                return False

        return True        


# @lc code=end

# LC 145 postorder DFS on tree may help! 


# We'd model each course as a node and each prerequisite relationship as a directed edge, 
# then run DFS from every course, tracking two sets: path, which holds nodes currently on 
# the active recursion stack, and visit, which holds nodes already proven safe. If we land 
# on a node still in path, that's a genuine cycle and we'd return false immediately; if we 
# land on a node in visit, it's already been fully resolved through some other branch and 
# we can short-circuit to true without re-exploring it. 


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

# dfs(0)
#   dfs(1)
#     dfs(3)
#       dfs(4) ✓ base
#     ← backtrack(3)
#     dfs(4) ✓ base
#   ← backtrack(1)
#   dfs(2) ✓ base
# ← backtrack(0)


# e.g., 
# prerequisites = [[0,1],[1,2],[2,0]]
# prereq_map = 
# crs pre
# 0   [1]
# 1   [2]
# 2   [0]


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

