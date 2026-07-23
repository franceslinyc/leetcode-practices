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

            res.append(node.val)  # Between left, right DO something

            dfs(node.right)

            # no return needed
        
        dfs(root)

        return res


        # # method 1 without dfs(node)

        # if not root:
            
        #     return []

        # return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        
        #        # + list concatenation, not addition


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
#   dfs(2)
#     dfs(4)
#       dfs(None) ✓ base
#     ← append(4),  res=[4]
#       dfs(None) ✓ base
#   ← append(2),    res=[4,2]
#     dfs(5)
#       dfs(6)
#         dfs(None) ✓ base
#       ← append(6),  res=[4,2,6]
#         dfs(None) ✓ base
#     ← append(5),    res=[4,2,6,5]
#       dfs(7)
#         dfs(None) ✓ base
#       ← append(7),  res=[4,2,6,5,7]
#         dfs(None) ✓ base
# ← append(1),        res=[4,2,6,5,7,1]
#   dfs(3)
#     dfs(None) ✓ base
#   ← append(3),    res=[4,2,6,5,7,1,3]
#     dfs(8)
#       dfs(9)
#         dfs(None) ✓ base
#       ← append(9),  res=[4,2,6,5,7,1,3,9]
#         dfs(None) ✓ base
#     ← append(8),    res=[4,2,6,5,7,1,3,9,8]
#       dfs(None) ✓ base
