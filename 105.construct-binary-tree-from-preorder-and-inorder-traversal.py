#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # method 1 dfs: O(n^2) time; O(n) space

        if not preorder or not inorder: 

            return None
        
        root = TreeNode(preorder[0])

        mid = inorder.index(preorder[0]) # .index() return the index of the value 

        root.left = self.buildTree(preorder[1 : mid + 1], # First part of preorder excluding root
                                   
                                   inorder[:mid])         # Remaining part of inorder

        root.right = self.buildTree(preorder[mid + 1 :],  # Second part of preorder
                                    
                                    inorder[mid + 1 :])   # Remaining part of inorder

        return root


        # method 2 dfs + hash map: O(n) time; O(n) space

        # method 3 dfs, optimized: O(n) time; O(n) space
        
# @lc code=end

