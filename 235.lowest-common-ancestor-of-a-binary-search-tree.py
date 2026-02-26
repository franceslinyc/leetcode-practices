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
        
        # # method 1 recrusivetime O(h), space O(h), where h: height of tree

        # if not root or not p or not q: # if not root: 

        #     return None
        
        # if p.val < root.val and q.val < root.val: 

        #     return self.lowestCommonAncestor(root.left, p, q)
        
        # elif p.val > root.val and q.val > root.val: 

        #     return self.lowestCommonAncestor(root.right, p, q)

        # else: 

        #     return root
        
    
        # method 2 iterative: time O(h), space O(1), where h: height of tree; space O(1) because no need of backtrack

        current = root

        while current: 

            if p.val < current.val and q.val < current.val:   # Search the left subtree

                current = current.left

            elif p.val > current.val and q.val > current.val: # Search the right subtree

                current = current.right

            else: # cover all cases when 
                  # p & q split across left & right 
                  # p or q equal to current 
                return current


# @lc code=end

