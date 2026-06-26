#
# @lc app=leetcode id=261 lang=python3
#
# [261] Graph Valid Tree
#

# @lc code=start
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # method 1 DFS + Cycle Detection: O(V + E) time; O(V + E) space
        
        if len(edges) != n - 1: 

            return False
        
        adj = defaultdict(list)

        for u, v in edges: 

            adj[u].append(v)          # Undirected edge; Record the connection from BOTH ends

            adj[v].append(u)

        visit = set()

        def dfs(node, prev):          # parent (or prev)

            if node in visit:         # Detect a loop, return False

                return False

            visit.add(node)

            for nei in adj[node]:
                
                if nei == prev:        # Skip if neighbor is parent (or prev)
                    
                    continue
                
                if not dfs(nei, node): # Propagate cycle found deeper in recursion; Recursively visit this neighbor's neighbor's neighbor's... till base cases.
                    
                    return False

            return True                

        return dfs(0, -1) and len(visit) == n


# @lc code=end

