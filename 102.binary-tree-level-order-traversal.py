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

        # method 1 DFS

        # method 2 BFS 

        if not root: 
            return []
        
        q = deque([root])

        res = []

        while q: 

            level = []

            for i in range(len(q)): # Process each node in the current level

                node = q.popleft()  # Pops exactly that many nodes

                level.append(node.val) 

                if node.left: 

                    q.append(node.left) 

                if node.right: 

                    q.append(node.right) 

            res.append(level) 
            
        return res

        # method 3 BFS

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

