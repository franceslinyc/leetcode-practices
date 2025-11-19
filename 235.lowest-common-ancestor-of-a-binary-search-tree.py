#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        current = root

        while current: 

            if p.val < current.val and q.val < current.val: 

                current = current.left

            elif p.val > current.val and q.val > current.val: 

                current = current.right

            else: # cover all cases when 
                  # p & q split across left & right 
                  # p or q equal to current 
                return current 


# @lc code=end

