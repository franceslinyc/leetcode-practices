#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.res = 0 

        def dfs(curr): 

            if not curr: 
                return 0 

            left = dfs(curr.left)     # Recursively find height of left and right subtrees
            right = dfs(curr.right)

            self.res = max(self.res, left + right) # Update res

            return max(left, right) + 1  # Return height to parent (current) node; + 1 for parent (current) node
        
        dfs(root)

        return self.res
        
# @lc code=end

