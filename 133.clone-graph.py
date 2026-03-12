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
        
        # # method 1 dfs: space O(V+E), where V = #s of vertices, E = #s of edges; space O(V)

        # this_map = {}

        # def dfs(node): 

        #     if node in this_map: 

        #         return this_map[node]                 # Return the clone if it exists. Otherwise, create the clone. 

        #     copy = Node(node.val)

        #     this_map[node] = copy

        #     # Recursively clone all neighbors

        #     for neighbor in node.neighbors: 

        #         copy.neighbors.append(dfs(neighbor))  # Append the cloned neighbor to the copy's neighbors list 

        #     return copy

        # return dfs(node) if node else None


        # method 2 bfs

        if not node: 

            return None

        this_map = {}

        this_map[node] = Node(node.val) # Without Node() cannot access neighbors 

        q = deque([node])

        while q: 

            current = q.popleft()

            for neighbor in current.neighbors: 

                # If the neighbor has not be cloned yet, make the clone and add neighbor to the queue to process its neighbors
                
                if neighbor not in this_map: 

                    this_map[neighbor] = Node(neighbor.val)

                    q.append(neighbor)

                # Otherwise, link the clone of the current node to the clone of the neighbor

                this_map[current].neighbors.append(this_map[neighbor]) # Not current.neighbors since current is "original" node, but we want "copy" or "clone" of current node

        return this_map[node] # Return the cloned version of the starting node


# 1 --- 2
# |     |
# 3 --- 4
#
# DFS:
# 
# BFS: 
#
# Idea: 
# 
# Details for DFS: 
#
# node1.neighbors = [node2, node3]
# copy1 = node1 
# for loop 
#   copy1.neighbors.append(copy2) -> copy1.neighbors = [copy2]
#   copy1.neighbors.append(copy3) -> copy1.neighbors = [copy2, copy3]
# copy1.neighbors = [copy2, copy3]


# @lc code=end

