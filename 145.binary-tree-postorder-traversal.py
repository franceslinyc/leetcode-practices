#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # method 1 dfs: O(n) time; O(n) space

        res = []

        def dfs(node): 

            if not node: 

                return

            dfs(node.left)

            dfs(node.right)

            res.append(node.val)

            # no return needed

        dfs(root)

        return res 
                
        
# @lc code=end


# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
# Output: [4,6,7,5,2,9,8,3,1]

#         1
#        / \
#       2   3
#      / \   \
#     4   5   8
#        / \ /
#       6  7 9

# dfs(1)
#   dfs(2)
#     dfs(4)
#       dfs(None) ✓ base
#       dfs(None) ✓ base
#     ← append(4),  res=[4]
#     dfs(5)
#       dfs(6)
#         dfs(None) ✓ base
#         dfs(None) ✓ base
#       ← append(6),  res=[4,6]
#       dfs(7)
#         dfs(None) ✓ base
#         dfs(None) ✓ base
#       ← append(7),  res=[4,6,7]
#     ← append(5),  res=[4,6,7,5]
#   ← append(2),    res=[4,6,7,5,2]
#   dfs(3)
#     dfs(None) ✓ base
#     dfs(8)
#       dfs(9)
#         dfs(None) ✓ base
#         dfs(None) ✓ base
#       ← append(9),  res=[4,6,7,5,2,9]
#     ← append(8),    res=[4,6,7,5,2,9,8]
#   ← append(3),    res=[4,6,7,5,2,9,8,3]
# ← append(1),      res=[4,6,7,5,2,9,8,3,1]