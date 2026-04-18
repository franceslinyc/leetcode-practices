#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(current): 

            # Base case: an empty node is balanced with height 0
            if not current: 

                return [True, 0] 

            # Recursively check left and right subtrees 
            left = dfs(current.left)

            right = dfs(current.right)

            # A tree is balanced if height difference is <= 1
            # left[1] -> height of left subtree
            # right[1] -> height of right subtree
            # left[0] -> whether left subtree is balanced
            # right[0] -> whether right subtree is balanced
            balanced = (abs(left[1] - right[1]) <= 1 and left[0] and right[0])

            # Return height of parent (current) node = max height of children + 1 
            return [balanced, max(left[1], right[1]) + 1]

        return dfs(root)[0]


# @lc code=end

