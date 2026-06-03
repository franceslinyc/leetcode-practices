#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # method 1 dfs: O(n) time; O(n) space

        res = []

        def dfs(node): 

            if not node: 

                return
            
            dfs(node.left)

            res.append(node.val)

            dfs(node.right)

            return res
        
        dfs(root)

        return res


# @lc code=end


# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
# Output: [4,2,6,5,7,1,3,9,8]

#         1
#       /   \
#      2     3
#     / \     \
#    4   5     8
#       / \   /
#      6   7 9

# dfs(1)
#   dfs(2)                         ← go left from 1
#     dfs(4)                       ← go left from 2
#       dfs(None)                  ← 4 has no left, base case return
#       append 4  ✓                ← visit 4
#       dfs(None)                  ← 4 has no right, base case return
#     append 2    ✓                ← left subtree of 2 done, visit 2
#     dfs(5)                       ← go right from 2
#       dfs(6)                     ← go left from 5
#         dfs(None)                ← 6 has no left, base case return
#         append 6  ✓              ← visit 6
#         dfs(None)                ← 6 has no right, base case return
#       append 5    ✓              ← left subtree of 5 done, visit 5
#       dfs(7)                     ← go right from 5
#         dfs(None)                ← 7 has no left, base case return
#         append 7  ✓              ← visit 7
#         dfs(None)                ← 7 has no right, base case return
#   append 1        ✓              ← left subtree of 1 done, visit 1
# 
# ...

