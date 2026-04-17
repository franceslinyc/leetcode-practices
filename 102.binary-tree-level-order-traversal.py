#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # # method 1 DFS: time O(n), space O(n), where n: # of nodes 

        # res = []

        # def dfs(node, depth):

        #     # Base case

        #     if not node:

        #         return None

        #     # Create a new list for this level if this is a first-time visit

        #     if len(res) == depth:

        #         res.append([])

        #     # Add current node's value to its corresponding level
            
        #     res[depth].append(node.val)

        #     # Recurse to the left and right child by increasing depth

        #     dfs(node.left, depth + 1)

        #     dfs(node.right, depth + 1)

        # # Start dfs from root at depth 0 

        # dfs(root, 0)

        # return res


        # method 2 BFS: time O(n), space O(n), where n: # of nodes; balanced BFS -> time O(log n)

        if not root:          # Careful! Not to miss edge cases

            return []
        
        res = []

        q = deque([root])

        while q: # Continue if there are still nodes to process

            level = []

            for i in range(len(q)): # Process each node in the current level

                # Process each node
                
                node = q.popleft()  # Pops exactly that many nodes

                level.append(node.val) 

                # Add children to queue
                
                if node.left: 

                    q.append(node.left) 

                if node.right: 

                    q.append(node.right) 

            res.append(level) 
            
        return res


# This problem can be solved using Breadth-First Search with a queue. We process nodes level by 
# level, from left to right. At each iteration, we use the queue size to determine how many 
# nodes belong to the current level. We collect their values, add their children, and repeat 
# until the queue is empty. Time complexity is O(n), and space complexity is O(n).


# BFS: 
# 
# 1. Build tree level by level
# 2. Use queue to find the path
# 3. Work on the concept of FIFO


# Details: 
# 
#     3
#    / \ 
#   9  20
#      / \     
#     15 17
#
# First while q: 
# node = 3
# q = []
# q = [9,20]
# level = [3]
# res = [[3]]
#
# Second while q: 
# node = 9
# q = [20]
# q = [20]     # 9 has no children
# level = [9]
# node = 20    # since q is not empty
# q = []
# q = [15, 17] # 20 has children
# level = [9,20]
# res = [[3], [9,20]]
#
# ...


# @lc code=end

