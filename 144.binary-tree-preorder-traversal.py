#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # method 1 dfs: O(n) time; O(n) space

        res = []

        def dfs(node): 

            if not node: 

                return

            res.append(node.val)

            dfs(node.left)

            dfs(node.right)

            return res

        dfs(root)

        return res
            
        
# @lc code=end


# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
# Output: [1,2,4,5,6,7,3,8,9]

#         1
#       /   \
#      2     3
#     / \     \
#    4   5     8
#       / \   /
#      6   7 9


# dfs(1)
#   append 1        ✓              ← visit 1 first (root)
#   dfs(2)                         ← go left from 1
#     append 2      ✓              ← visit 2 first (root of subtree)
#     dfs(4)                       ← go left from 2
#       append 4    ✓              ← visit 4 first (root of subtree)
#       dfs(None)                  ← 4 has no left, base case return
#       dfs(None)                  ← 4 has no right, base case return
#     dfs(5)                       ← go right from 2
#       append 5    ✓              ← visit 5 first (root of subtree)
#       dfs(6)                     ← go left from 5
#         append 6  ✓              ← visit 6 first (root of subtree)
#         dfs(None)                ← 6 has no left, base case return
#         dfs(None)                ← 6 has no right, base case return
#       dfs(7)                     ← go right from 5
#         append 7  ✓              ← visit 7 first (root of subtree)
#         dfs(None)                ← 7 has no left, base case return
#         dfs(None)                ← 7 has no right, base case return
#   dfs(3)                         ← go right from 1
#     append 3      ✓              ← visit 3 first (root of subtree)
#     dfs(None)                    ← 3 has no left, base case return
#     dfs(8)                       ← go right from 3

# ...