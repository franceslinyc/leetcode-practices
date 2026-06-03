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

