#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        # method 1 dfs

        if not node: 
            return None

        this_map = {}

        def dfs(node): 

            if node in this_map: 
                return this_map[node]
            
            copy = Node(node.val) # Careful, not just Node(node)
            this_map[node] = copy

            #copy.neighbors = []  # See class Node above 
            for neighbor in node.neighbors: 
                copy.neighbors.append(dfs(neighbor))
            return copy
        
        return dfs(node)    

        # method 2 bfs


# 1 --- 2
# |     |
# 3 --- 4
#
# node1.neighbors = [node2, node3]
# copy1 = node1 
# for loop 
#   copy1.neighbors.append(copy2) -> copy1.neighbors = [copy2]
#   copy1.neighbors.append(copy3) -> copy1.neighbors = [copy2, copy3]
# copy1.neighbors = [copy2, copy3]


# @lc code=end

