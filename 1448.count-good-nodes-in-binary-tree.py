#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, max_val):

            # Base case
            if not node: 

                return 0 

            # Check if current node is good, i.e., a node is good when its value >= max value seen so far 
            res = 1 if node.val >= max_val else 0 

            max_val = max(max_val, node.val)

            # Recursively count good nodes in left and right subtree 
            res += dfs(node.left, max_val)

            res += dfs(node.right, max_val)

            return res 

        return dfs(root, root.val)
        

# @lc code=end


#     3
#    / \
#   1   4
#      / \
#     1   5

# 3 -> good (first node)
# 1 -> not good (less than 3)
# 4 -> good (>= 3)
# 1 -> not good (less than 4)
# 5 -> good (>= 4)