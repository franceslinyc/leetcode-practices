#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # # method 2 dfs: O(n) time; O(n) space 
        # # inorder traversal, i.e., left -> root -> right

        # res = []

        # def dfs(node): 

        #     if not node: 

        #         return 
            
        #     dfs(node.left)

        #     res.append(node.val)

        #     dfs(node.right)

        # dfs(root)

        # return res[k-1]
    

        # method 3 recursive dfs, optimized: O(k + h) time, O(n) worst case; O(h) space

        res = root.val 

        count = k

        def dfs(node): 

            nonlocal res, count

            if not node: 

                return 
            
            dfs(node.left)

            if count == 0: # If k-th smallest already found in left subtree

                return     # Exit, no need to keep going 
                        
            # vs method 2: Instead of res.append(node.val), discount and store res 
            
            count -= 1

            if count == 0: # If this is the k-th smallest

                res = node.val

                return     # Exit, no need to go right 

            dfs(node.right)

        dfs(root)

        return res

# @lc code=end
