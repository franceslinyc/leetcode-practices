#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # method 1 recursive DFS

        if not root: 
            return None
        
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

        # # method 2 BFS

        # if not root: 
        #     return None
        
        # q = deque([root])

        # while q: 
        #     node = q.popleft()

        #     tmp = node.left
        #     node.left = node.right
        #     node.right = tmp

        #     if node.left: 
        #         q.append(node.left)

        #     if node.right: 
        #         q.append(node.right)
    
        # return root

        # # method 3 iterative DFS

        # if not root: 
        #     return None
        
        # s = [root]

        # while s: 

        #     node = s.pop()

        #     tmp = node.left
        #     node.left = node.right
        #     node.right = tmp

        #     if node.left: 
        #         s.append(node.left)

        #     if node.right: 
        #         s.append(node.right)

        # return root

    
# @lc code=end

