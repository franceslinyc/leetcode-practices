#
# @lc app=leetcode id=261 lang=python3
#
# [261] Graph Valid Tree
#

# @lc code=start
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1: 

            return False
        

        adj = defaultdict(list)

        for u, v in edges: 

            adj[u].append(v)         # Undirected edge; record the connection from BOTH ends

            adj[v].append(u)

        visit = set()

        def dfs(node, parent):       # parent (or prev)

            if node in visit:        # Detect a loop

                return False

            visit.add(node)

            for nei in adj[node]:
                
                if nei == parent:      # Skip if neighbor is parent (or prev)
                    
                    continue
                
                if not dfs(nei, node): # Detect a loop
                    
                    return False

            return True                

        return dfs(0, -1) and len(visit) == n


# @lc code=end

