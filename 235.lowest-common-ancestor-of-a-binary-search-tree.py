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
        
        # # method 1 recrusive
        # if not root or not p or not q: # if not root: 

        #     return None
        
        # if p.val < root.val and q.val < root.val: 

        #     return self.lowestCommonAncestor(root.left, p, q)
        
        # elif p.val > root.val and q.val > root.val: 

        #     return self.lowestCommonAncestor(root.right, p, q)

        # else: 

        #     return root
        
    
        # method 2 iterative
        curr = root

        while curr: 

            if p.val < curr.val and q.val < curr.val: 

                curr = curr.left

            elif p.val > curr.val and q.val > curr.val: 

                curr = curr.right

            else: # cover all cases when 
                  # p & q split across left & right 
                  # p or q equal to current 
                return curr


# @lc code=end

