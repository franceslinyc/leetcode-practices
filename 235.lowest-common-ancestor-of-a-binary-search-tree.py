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
        
        # # method 1 recrusive: time O(h), space O(h), where h: height of tree

        # if not root or not p or not q: # if not root: 

        #     return None 
        
        # if p.val < root.val and q.val < root.val: 

        #     return self.lowestCommonAncestor(root.left, p, q)
        
        # elif p.val > root.val and q.val > root.val: 

        #     return self.lowestCommonAncestor(root.right, p, q)

        # else: 

        #     return root


        # method 1 recrusive: time O(h), space O(h), where h: height of tree
     
        def dfs(node):

            if not node:
                
                return None

            if node.val > p.val and node.val > q.val:

                return dfs(node.left)
            
            elif node.val < p.val and node.val < q.val:

                return dfs(node.right)
            
            else:

                return node
        
        return dfs(root)
        
    
        # # method 2 iterative: time O(h), space O(1), where h: height of tree; space O(1) because no need of backtrack

        # current = root

        # while current: 

        #     if current.val > p.val and current.val > q.val:   # current too big -> search the left subtree

        #         current = current.left

        #     elif current.val < p.val and current.val < q.val: # current too small -> search the right subtree

        #         current = current.right

        #     else: # cover all cases when 
        #           # p & q split across left & right 
        #           # p or q equal to current 
        #         return current


# @lc code=end


# Since it’s a BST, we can use current as a pointer to traverse the tree. Starting from the
# root, if both nodes are smaller, we go to the left subtree. If both nodes are greater, 
# we'd go to the right subtree. If they split, the current node is the LCA. This gives us 
# O(h) time complexity and O(h) space for recrusive method. O(1) space for iterative method.


# Ques: 
# 
# 1. Are p and q guaranteed to exist in the tree?
# 2. Can a node be an ancestor of itself?


# BST: 
# 
# 1. Left subtree's value < current's 
# 2. Right subtree's value > current's
# 3. Both left and right substree are also BSTs.
