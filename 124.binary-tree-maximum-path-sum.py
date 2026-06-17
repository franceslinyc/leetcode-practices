#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        # method 2 dfs, optimized: O(n) time; O(n) space; post-order traversal

        res = root.val  # Careful! res = float('-inf') works too

        def dfs(node):

            nonlocal res

            if not node:

                return 0

            left = max(dfs(node.left), 0) # Ignore negative contributions

            right = max(dfs(node.right), 0)

            # Update best path *through* node 
            res = max(res, node.val + left + right)

            # Return best single-branch gain to parent, i.e., node.val (current node) + max gain of children
            return node.val + max(left, right)

        dfs(root)

        return res


# @lc code=end

# Every "best path in a tree" problem has this split:
# 1. Best path through node — use both branches, bend here, update global answer
# 2. Best single branch — picks one side, return to parent so it can do its calculation


# 1. "What's the best path through me?" -> update global
# 2. "What can I offer my parent?" -> return value