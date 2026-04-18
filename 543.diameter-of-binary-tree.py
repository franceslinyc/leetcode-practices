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

        self.diameter = 0 

        def dfs(current): 

            # Base case: empty node has height 0
            if not current: 

                return 0 

            # Recursively find height of left and right subtrees
            left = dfs(current.left)        
            
            right = dfs(current.right)

            self.diameter = max(self.diameter, left + right) # Update diameter

            # Return height of parent (current) node = max height of children + 1 
            return max(left, right) + 1  
        
        dfs(root)

        return self.diameter


# @lc code=end

