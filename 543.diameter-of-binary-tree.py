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

        # method 1 recursive DFS: O(n) time worst case, O(log n) best case; O(n) space; post-order traversal

        diameter = 0 

        def dfs(node): 

            nonlocal diameter
            
            # Base case: empty node has height 0
            if not node: 

                return 0 

            # Recursively find height of left and right subtrees
            left = dfs(node.left)        
            
            right = dfs(node.right)

            # Update diameter
            diameter = max(diameter, left + right) 

            # Return height of current node to parent, i.e., 1 (edge to parent) + max height of children
            return 1 + max(left, right) 
        
        dfs(root)

        return diameter


        # method 2 DFS with Stack: O(n) time; O(n) space


# @lc code=end


# 1. "What's the best path through me?" -> update global

# 2. "What can I offer my parent?" -> return value