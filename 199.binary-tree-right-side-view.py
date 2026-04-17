#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # method 1 bfs

        if not root: 

            return []
        
        q = deque([root])

        res = []

        while q: 

            rightside = None         # vs LC 102 level = [] 

            for i in range(len(q)): 

                node = q.popleft()

                rightside = node.val # Keep overwriting; vs LC 102 level.append(node.val) store the entire level

                if node.left: 

                    q.append(node.left)
                
                if node.right: 

                    q.append(node.right)

            res.append(rightside)    # Safer to add instead of adding node.val directly 
            
        return res

    
        # # method 2 dfs

        # res = []

        # def dfs(node, depth): 

        #     if not node: 
        #         return None
            
        #     if depth == len(res):      # If this is the first time reaching this depth, store it
        #         res.append(node.val)
            
        #     dfs(node.right, depth + 1) # Go right first
        #     dfs(node.left, depth + 1)
        
        # dfs(root, 0)

        # return res 


# BFS: 
# 1. Build tree level by level
# 2. Use queue to find the path
# 3. Work on the concept of FIFO
#
# Idea: 
# This problem can be solved using Breadth-First Search with a queue.
# We process nodes level by level.
# At each iteration, we use the queue size to determine how many nodes belong to the current level.
# We process all nodes in that level and add their children. 
# The last node processed in that level is the rightmost node,
# so we add its value to the result list.
# Then we repeat until the queue is empty.
# Time complexity is O(n), and space complexity is O(n).


# @lc code=end

