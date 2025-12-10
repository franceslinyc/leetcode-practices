#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # method 1 bfs
        if not root: 
            return None
        
        q = deque([(root, float("-Inf"), float("Inf"))])

        while q: 
            node, left, right = q.popleft()

            if not (left < node.val < right): 
                return False
            
            if node.left: 
                q.append((node.left, left, node.val))    # update right boundary
            
            if node.right: 
                q.append((node.right, node.val, right))  # update left boundary
        
        return True

        # method 2 dfs


#                    5        -Inf < 5 < Inf
#                   / \
# -Inf < 3 < 5     3   7      5 < 7 < Inf
#                     / \
# 5 < 4 < 7 Fails    4   8    7 < 8 < Inf 

        
# @lc code=end

