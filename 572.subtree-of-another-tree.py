#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # method 1 dfs: O(m * n) time; O(m + n) space, where m is # of nodes in subRoot, n is # of nodes in root

        if not subRoot: 

            return True

        if not root: 

            return False

        def isSameTree(p, q):

            if not p and not q:

                return True

            if not p or not q or p.val != q.val:

                return False

            # Recursively check if left AND right subtrees are identical 

            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        if isSameTree(root, subRoot):

            return True

        # Recursively check if subRoot exists deeper in left OR right subtree

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)        

        
# @lc code=end

