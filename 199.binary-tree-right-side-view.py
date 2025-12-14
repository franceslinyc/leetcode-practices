#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # method 1 bfs

        if not root: 

            return []
        
        q = deque([root])

        res = []

        while q: 

            rightside = None         #level = [] vs LC 102

            for i in range(len(q)): 

                node = q.popleft()

                rightside = node.val #level.append(node.val) vs LC 102

                if node.left: 

                    q.append(node.left)
                
                if node.right: 

                    q.append(node.right)

            res.append(rightside)    # Safer to add instead of adding node.val directly 
            
        return res
    
        # # method 2 dfs

        # res = []

        # def dfs(node, depth): 

        #     if not node: 
        #         return None
            
        #     if depth == len(res):      # If this is the first time reaching this depth, store it
        #         res.append(node.val)
            
        #     dfs(node.right, depth + 1) # Go right first
        #     dfs(node.left, depth + 1)
        
        # dfs(root, 0)

        # return res 


# @lc code=end

