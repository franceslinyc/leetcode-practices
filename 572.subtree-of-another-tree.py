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

        if not root and subRoot: 

            return False
        
        if not subRoot: 

            return True

        def isSameTree(node, subNode):

            if not node and not subNode:

                return True

            if not node or not subNode or node.val != subNode.val:

                return False

            # Recursively check left AND right subtrees match

            return (isSameTree(node.left, subNode.left) and # Don't need self. here!

                    isSameTree(node.right, subNode.right))

        if isSameTree(root, subRoot):

            return True

        # Recursively check if subRoot exists deeper in left OR right subtree

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)        

        
# @lc code=end

